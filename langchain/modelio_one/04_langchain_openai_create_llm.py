"""
    测试在LangChain中获取大模型对象的两种方式
    1、init_chat_model()
    2、使用LangChain和各个大模型结合的集成包所提供的类型获取
        OpenAI-->langchain-openai-->ChatOpenAI
        DeepSeek-->langchain-deepseek-->ChatDeepSeek
"""
import os

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

# llm = init_chat_model(
#     model="gpt-4o-mini",
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url=os.getenv("OPENAI_API_BASE_URL"),
# )
#
# result = llm.invoke("讲一个笑话")
#
# print(result)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL"),
)

result = llm.invoke("什么是agent")

print(result.content)