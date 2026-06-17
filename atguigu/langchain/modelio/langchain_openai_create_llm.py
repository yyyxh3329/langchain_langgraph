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

# 创建大模型对象方式1：
# llm = init_chat_model(
#     model="gpt-4o-mini",
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url=os.getenv("OPENAI_BASE_URL"),
# )

# 创建大模型对象，会自动获取环境变量中OPENAI_API_KEY和OPENAI_BASE_URL所对应的环境变量的值
# llm = init_chat_model(
#     model="gpt-4o-mini"
# )

# 创建大模型对象方式2：
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url=os.getenv("OPENAI_BASE_URL")
# )

# 创建大模型对象方式2：
llm = ChatOpenAI(
    model="gpt-4o-mini"
)


# 调用大模型
result = llm.invoke("给我讲个笑话")

print(result.content)