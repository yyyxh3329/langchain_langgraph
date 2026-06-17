from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

prompt_message = PromptTemplate.from_template("你是一个专业的商品评价师,请从{aspect1}和{aspect1}方面来对{product}评价")

message = prompt_message.invoke(
    {
        "aspect1": "性价比",
        "aspect2": "性能",
        "product": "拯救者Y9000"
    }
)

result = llm.invoke(message)
print(result)