from FlagEmbedding import BGEM3FlagModel
from langchain_community.chat_models import ChatOpenAI
from pymilvus import MilvusClient, RRFRanker, AnnSearchRequest


def get_milvus_client():
    return MilvusClient(
        uri="http://localhost:19530",
    )


def query_to_vector(query):
    # 创建嵌入模型实例
    embed_model = BGEM3FlagModel(
        model_name_or_path=r"D:\BaiduNetdiskDownload\尚硅谷大模型260318线上同步\14_尚硅谷大模型技术之LangChain\2.资料\bge-m3"
    )
    all_vector = embed_model.encode(
        sentences=query,
        return_dense=True,
        return_sparse=True,
    )
    return all_vector["dense_vecs"], all_vector["lexical_weights"]


def search_dense_vector(client: MilvusClient, collection_name, query):
    """通过稠密向量进行检索"""
    dense_vecs, _ = query_to_vector(query)
    result = client.search(
        collection_name=collection_name,
        # 这里的输入需要的是 变成二维列表，传过来的是一维列表，可以在前面改，也可以在这里改
        data=[dense_vecs],  # 要检索的数据
        anns_field="vector",  # 要检索的字段
        limit=3,  # topK
        search_params={"metric_type": "L2"},  # 设置检索的方式
        output_fields=["id", "text", "metadata"]
    )

    print(result)


def search_sparse_vector(client: MilvusClient, collection_name, query):
    """通过稀疏向量进行检索"""
    _, sparse_vector = query_to_vector(query)
    result = client.search(
        collection_name=collection_name,
        # 这里的输入需要的是 变成二维列表，传过来的是一维列表，可以在前面改，也可以在这里改
        data=[sparse_vector],  # 要检索的数据
        anns_field="sparse_vector",  # 要检索的字段
        limit=3,  # topK
        search_params={"metric_type": "IP"},  # 设置检索的方式
        output_fields=["id", "text", "metadata"]
    )

    print(result)

def hybrid_search_vector(client: MilvusClient, collection_name, query):
    """通过稠密向量和稀疏向量进行混合检索"""
    dense_vector,sparse_vector = query_to_vector(query)
    dense_vector_req = AnnSearchRequest(
        data=[dense_vector],
        anns_field="vector",
        param={"metric_type": "L2"},
        limit=3
    )

    sparse_vector_req = AnnSearchRequest(
        data=[sparse_vector],
        anns_field="sparse_vector",
        param={"metric_type": "IP"},
        limit=3
    )


    result = client.hybrid_search(
        collection_name=collection_name,
        reqs=[dense_vector_req, sparse_vector_req], # 设置检索条件
        ranker=RRFRanker(),  # 设置重排规则
        limit=3,
        output_fields=["id", "text", "metadata"]

    )

    print(result)
    return result

def final_generate(client: MilvusClient, collection_name, query):
    results = hybrid_search_vector(client,collection_name,query)

    llm = ChatOpenAI(
        model="gpt-4o-mini"
    )
    # 整理上下文
    content = "\n".join([result['entity']['text'] for result in results[0]])

    response = llm.invoke(
        [
            ("user",f"请根据上下文总结回答：上下文：{content}，问题：{query}"),
        ]
    )

    print(response)

if __name__ == '__main__':
    client = get_milvus_client()
    # search_dense_vector(client, "milvus_collection", "监护人要履行什么职责")
    # search_sparse_vector(client, "milvus_collection", "监护人要履行什么职责")
    # hybrid_search_vector(client, "milvus_collection", "监护人要履行什么职责")
    final_generate(client, "milvus_collection", "监护人要履行什么职责")
