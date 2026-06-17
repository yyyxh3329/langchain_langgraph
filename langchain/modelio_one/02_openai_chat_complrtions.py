"""
    测试
"""
import os

from openai import OpenAI



client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_URL"),
)

result = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":"给我将一个笑话"
        }
    ]
)

print(result)

