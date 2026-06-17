"""
    调用大模型的四种方式：
    1、invoke()，同步调用
    2、ainvoke()，异步调用
    3、stream()，流式调用
    4、batch()，批次调用
"""
import asyncio

from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini"
)

result = llm.batch(
    [
        [
            ("user","什么是LangChain")
        ],
        [
            ("user","什么是向量数据库")
        ]
    ]
)

for i in result:
    print(i.content)



