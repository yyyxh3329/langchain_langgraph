from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel(
    model_name_or_path=r"D:\BaiduNetdiskDownload\尚硅谷大模型260318线上同步\14_尚硅谷大模型技术之LangChain\2.资料\bge-m3")

res = model.encode(
    ["标量字段通常用来存储一些元数据，并可以在搜索时通过元数据进行过滤","我喜欢大模型"],
    return_sparse=True,
    return_dense=True)
print('encode结果为：', res, end='\n\n')
# 1、打印稀疏向量
print('稀疏向量为：', res["lexical_weights"], end='\n\n')
# 2、将稀疏向量当中的id转换为token，并打印
sparse_vecs = model.convert_id_to_token(res["lexical_weights"])
print('稀疏向量转换为token后的结果为：', sparse_vecs, end='\n\n')
# 3、打印稠密向量
print('稠密向量为：', res["dense_vecs"], end='\n\n')
