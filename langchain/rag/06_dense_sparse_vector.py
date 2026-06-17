from FlagEmbedding import BGEM3FlagModel


# 创建模型对象
model = BGEM3FlagModel(
    model_name_or_path=r"D:\BaiduNetdiskDownload\尚硅谷大模型260318线上同步\14_尚硅谷大模型技术之LangChain\2.资料\bge-m3"
)

# 通过模型对象生成稠密向量和稀疏向量
result = model.encode(
    sentences="标量字段通常用来存储一些元数据，并可以在搜索时通过元数据进行过滤",
    return_dense=True,
    return_sparse=True
)

result1 = model.encode(
    sentences=["标量字段通常用来存储一些元数据，并可以在搜索时通过元数据进行过滤"],
    return_dense=True,
    return_sparse=True
)

print(result)
print(result['dense_vecs'])
print(result['lexical_weights'])

print("="*60)

print(result1['dense_vecs'])
print(result1['lexical_weights'])

for res,flo in result1['lexical_weights'][0].items():
    print("=" * 60)
    print(res,flo)
