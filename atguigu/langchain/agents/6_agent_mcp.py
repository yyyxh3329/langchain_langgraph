"""
    测试：使用agent调用MCPServer所提供的工具
"""
import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI


async def test():
    # 获取MCPServer的客户端
    client = MultiServerMCPClient(
        {
            "12306-mcp": {
                "transport": "streamable_http",
                "url": "https://mcp.api-inference.modelscope.net/3c853d48fd2c4d/mcp"
            }
        }
    )

    # 获取MCPServer所提供的所有的工具
    tools = await client.get_tools()

    # 创建llm
    llm = ChatOpenAI(
        model="gpt-4o-mini"
    )

    # 创建agent
    agent = create_agent(
        model=llm,
        tools=tools,
    )

    # 通过agent调用大模型
    result = await agent.ainvoke(
        {
            "messages":[
                ("user", "查询今天北京到武汉的车票，以表格的方式输出结果")
            ]
        }
    )

    print(result["messages"][-1].content)

asyncio.run(test())