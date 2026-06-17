"""
    测试使用ResponseAPI调用OPENAI（了解）
"""
from openai import OpenAI

# 创建调用大模型的客户端
client = OpenAI()

# 调用大模型
result = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role":"user",
            "content":"给我讲一个关于程序员的笑话 "
        }
    ]
)

print(result.output[0].content[0].text)