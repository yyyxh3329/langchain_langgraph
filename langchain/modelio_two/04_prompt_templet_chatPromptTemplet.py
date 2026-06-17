from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

chat_prompt_message = ChatPromptTemplate.from_messages(
    messages=[
        {
            "role": "system",
            "content": "你是一个专业的商品评价师",
        },
        {
            "role": "user",
            "content": "请从{aspect1}和{aspect1}方面来对{product}评价"
        }
    ]
)

chat_message = chat_prompt_message.invoke(
    {
        "aspect1": "性价比",
        "aspect2": "性能",
        "product": "拯救者Y9000"
    }
)

result = llm.invoke(chat_message)
print(result)

