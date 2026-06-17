"""
    测试调用大模型时设置提示词的方式：
    1、字符串
    2、字典
    [
        {
            "role":"system",
            "content":"xxx"
        },
        {
            "role":"user",
            "content":"xxx"
        }
    ]
    3、使用相对应的类型的实例对象表示系统提示词和用户提示词
    SystemMessage：表示系统提示词
    HumanMessage：表示用户提示词
    4、使用元组表示系统提示词和用户提示词
    ("system","xxx")
    ("user","xxx")

"""
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

# 设置提示词的方式1：
# result = llm.invoke("给我讲个笑话")

# 设置提示词的方式2：
# result = llm.invoke(
#     [
#         {
#             "role":"system",
#             "content":"你是一个笑话专家"
#         },
#         {
#             "role":"user",
#             "content":"给我讲一个笑话"
#         }
#     ]
# )

# 设置提示词的方式3：
# result = llm.invoke(
#     [
#         SystemMessage(content="你是一个笑话专家"),
#         HumanMessage(content="给我讲一个笑话")
#     ]
# )

# 设置提示词的方式4：
result = llm.invoke(
    [
        ("system", "你是一个笑话专家"),
        ("user", "给我讲一个笑话")
    ]
)

print(result.content)