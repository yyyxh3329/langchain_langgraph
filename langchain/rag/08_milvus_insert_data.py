from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pymilvus import MilvusClient
from FlagEmbedding import BGEM3FlagModel


def build_milvus_client():
    return MilvusClient(
        uri="http://localhost:19530",
    )


def insert_data(client: MilvusClient, collection_name: str):
    # 加载word文档
    documents = UnstructuredWordDocumentLoader(
        file_path="../../data/sample.docx",
        mode="single"
    ).load()

    # 对文档进行切分,此时的chunks是一个documents的list
    chunks = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", "。", "，", ""],
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    ).split_documents(documents)

    chunks = chunks[0:50]

    # 创建嵌入模型实例
    embed_model = BGEM3FlagModel(
        model_name_or_path=r"D:\BaiduNetdiskDownload\尚硅谷大模型260318线上同步\14_尚硅谷大模型技术之LangChain\2.资料\bge-m3"
    )
    # 使用bge-m3将数据片段转换为稠密向量和稀疏向量
    all_vector = embed_model.encode(
        sentences=[ chunk.page_content for chunk in chunks ],
        return_dense=True,
        return_sparse=True,
    )

    # 获取到稠密向量和稀疏向量
    # all_vectors:{"dense_vecs":[[指定维数的浮点],...], "lexical_weights":[[数据片段所对应的稀疏向量],...]}
    vectors = all_vector["dense_vecs"]
    sparse_vectors = all_vector["lexical_weights"]

    data_list = []
    for chunk,vector,sparse_vector in zip(chunks,vectors, sparse_vectors):
        data_list.append(
            {
                "vector": vector,
                "sparse_vector": sparse_vector,
                "text": chunk.page_content,
                "metadata": chunk.metadata,
            }
        )


    client.insert(
        collection_name=collection_name,
        data=data_list,
    )


if __name__ == '__main__':
    milvus_client = build_milvus_client()
    insert_data(milvus_client, "milvus_collection")
