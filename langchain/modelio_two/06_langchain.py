from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt_template = ChatPromptTemplate.from_messages(
    messages=[
        ("system", "你是一个专业的商品评价师"),
        ("user", "请从{aspect1}和{aspect1}方面来对{product}评价")
    ]
)
message = prompt_template.invoke(
    {
        "aspect1": "性价比",
        "aspect2": "性能",
        "product": "拯救者Y9000"
    }
)
llm = ChatOpenAI(
    model="gpt-4o-mini"
)
result = llm.invoke(message)

str_parse = StrOutputParser()
str_res = str_parse.invoke(result)
print(str_res)


