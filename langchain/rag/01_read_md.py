"""
    测试：解析markdown文件
    mode = "single | elements"
    single:将加载的文档中所有的内容加载为一个Document对象
"""

from langchain_community.document_loaders import UnstructuredMarkdownLoader

# 创建文档加载器
# loader = UnstructuredMarkdownLoader("../../data/sample.md",encoding="utf-8",mode="single")
#
# # 加载文档
# documents = loader.load()
#
# print(type(documents))  # list
# print(documents)

# for document in documents:
#     print(document)


loader = UnstructuredMarkdownLoader("../../data/sample.md",encoding="utf-8",mode="elements")
documents = loader.load()
# print(type(documents))
for document in documents:
    print(document)