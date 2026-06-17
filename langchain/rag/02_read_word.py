from langchain_community.document_loaders import UnstructuredWordDocumentLoader

loader = UnstructuredWordDocumentLoader("../../data/sample.docx",encoding="utf-8",mode="single")

documents = loader.load()
for document in documents:
    print(document)