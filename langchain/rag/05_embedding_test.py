"""
    测试：使用嵌入模型将文本转换为向量
"""
from langchain_huggingface import HuggingFaceEmbeddings

embed_model = HuggingFaceEmbeddings(
    model_name=r"D:\BaiduNetdiskDownload\尚硅谷大模型260318线上同步\14_尚硅谷大模型技术之LangChain\2.资料\assets\models\bge-base-zh-v1.5",
)

result = embed_model.embed_query("你好，世界")
print(result)
print(len(result))

result1 = embed_model.embed_documents(["你好世界","你好世界"])  # list[list[float]]
for res in result1:
    print(res)

