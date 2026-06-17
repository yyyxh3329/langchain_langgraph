from pymilvus import MilvusClient


def get_milvus_client():
    return MilvusClient(
        uri="http://localhost:19530",
    )


def milvus_delete(client: MilvusClient, collection_name):
    result = client.delete(
        collection_name=collection_name,
        filter="id in [466938680306268562, 466938680306268563]",
    )
    print(result)

def query_data(client: MilvusClient, collection_name):
    result = client.query(
        collection_name=collection_name,
        filter=" text like '%监护人%' ",
        output_fields=["id","text", "metadata"],
    )

    print(result)


if __name__ == '__main__':
    milvus_client = get_milvus_client()
    # milvus_delete(milvus_client, "milvus_collection")
    query_data(milvus_client, "milvus_collection")
