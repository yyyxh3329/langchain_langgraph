"""
    测试：在Milvus中创建Collection
    （1）构建schema信息；
    （2）添加索引；
    （3）创建collection。
"""
from attr.validators import max_len
from pymilvus import MilvusClient, DataType

# 创建milvus客户端
def get_milvus_client():
    return MilvusClient(
        uri="http://localhost:19530",
    )


# 构建milvus schema信息
def build_milvus_schema():
    return MilvusClient.create_schema(
        auto_id=True
    ).add_field(
        field_name="id", datatype=DataType.INT64, is_primary=True
    ).add_field(
        field_name="vector", datatype=DataType.FLOAT_VECTOR,dim=1024
    ).add_field(
        field_name="sparse_vector", datatype=DataType.SPARSE_FLOAT_VECTOR
    ).add_field(
        field_name="text", datatype=DataType.VARCHAR,max_length = 1500
    ).add_field(
        field_name="metadata", datatype=DataType.JSON
    )


# 构建collection index 索引
def build_milvus_index():
    index_params = MilvusClient.prepare_index_params()
    # 为稠密向量添加index
    index_params.add_index(
        field_name="vector",  # 创建索引的字段名
        index_type="HNSW",  # 索引的类型
        metric_type="L2",  # 根据索引检索是使用的检索方式
    )
    # 为稀疏向量添加index
    index_params.add_index(
        field_name="sparse_vector",
        index_type="SPARSE_INVERTED_INDEX",
        metric_type="IP",
    )

    return index_params


# 构建collection
def build_milvus_collection(client: MilvusClient, collection_name):
    client.create_collection(
        collection_name=collection_name,
        schema=build_milvus_schema(),
        index_params=build_milvus_index(),
    )
    print(client.list_collections())

if __name__ == '__main__':
    milvus_client = get_milvus_client()
    build_milvus_collection(milvus_client, "milvus_collection")
