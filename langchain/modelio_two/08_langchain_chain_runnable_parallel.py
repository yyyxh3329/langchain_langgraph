from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

llm = init_chat_model(
    model="gpt-4o-mini"
)

chain1 = PromptTemplate.from_template("把这个句子{topic}翻译成英文") | llm | StrOutputParser()
chain2 = PromptTemplate.from_template("把这个句子{topic}翻译成韩文") | llm | StrOutputParser()

map_chain = RunnableParallel(english=chain1, korean=chain2)
result = map_chain.invoke({"topic":"好好学习，天天向上"})
print(result)