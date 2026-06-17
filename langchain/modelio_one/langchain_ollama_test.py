from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:8b"
)

result =  llm.invoke(
    [
        ("user","你好")
    ]
)
print(result)