"""
    测试使用ChatCompletionsAPI调用OPENAI（了解）
"""

from openai import OpenAI

# 创建连接（调用）大模型的客户端
client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "什么是LangChain"
        }
    ]
)

print(result)
