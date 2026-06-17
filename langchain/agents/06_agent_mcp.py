"""
    测试：使用agent调用MCPServer所提供的工具
"""
import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI

async def get_mcp():
    # 获取MCPServer的客户端
    client = MultiServerMCPClient(
        {
            "12306-mcp": {
                    "transport": "streamable_http",
                    "url": "https://mcp.api-inference.modelscope.net/91ce00ae4ccb47/mcp"
                }
        }
    )

    # 获取MCPServer的所有工具
    tools = await client.get_tools()


    llm = ChatOpenAI(
        model="gpt-4o-mini",
    )

    agent = create_agent(
        model=llm,
        tools=tools,
    )

    result = await agent.ainvoke(
        input={
            "messages":[
                ("user", "查询今天北京到上海的车票，以表格的方式输出结果")
            ]
        }
    )

    print(result)


asyncio.run(get_mcp())
