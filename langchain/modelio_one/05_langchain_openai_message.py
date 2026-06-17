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
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

# 方式1
llm = init_chat_model(
    model="gpt-4o-mini",
)

# result1 = llm.invoke("什么是微调")
# print(result1.content)

# 方式2
# result2 = llm.invoke(
#     [
#         {
#             "role":"system",
#             "content":"你是一个大模型专家"
#         },
#         {
#             "role":"user",
#             "content":"解释下什么是微调"
#         }
#     ]
# )
# print(result2)

# 方式3
# result3 = llm.invoke(
#     [
#         SystemMessage(content="你是一个大模型专家"),
#         HumanMessage(content="什么是RAG")
#     ]
# )
# print(result3)

# 方式3
result4 = llm.invoke(
    [
        ("system","你是一个大模型专家"),
        ("user","什么是agent")
    ]
)

print(result4)