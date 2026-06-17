"""
    测试：使用agent调用本地工具
"""
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

load_dotenv()

# 创建Tavily搜索引擎实例，并设置最多查询5个结果
search = TavilySearch(max_results=5)

tools = [search]

# 创建智能体
agent = create_agent(
    model=llm,
    tools=tools,
)

result = agent.invoke(
    input={
        "messages":[
            ("system","你是位助手，需要调用工具来帮助用户。"),
            ("user", "查询上海今天的天气")
        ]
    }
)

print(result)