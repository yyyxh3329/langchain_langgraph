"""
    测试使用ChatCompletionsAPI调用OPENAI（了解）
"""
import os

from openai import OpenAI

# 创建连接（调用）大模型的客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

# 调用大模型
result = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":"什么是LangChain"
        }
    ]
)

print(result.choices[0].message.content)