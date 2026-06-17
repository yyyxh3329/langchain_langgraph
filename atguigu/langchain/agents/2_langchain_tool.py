"""
    测试：使用LangChain调用本地工具
"""
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# @tool(description="获取某个城市在某天的天气情况")
@tool
def get_weather(city, date):
    """获取某个城市在某天的天气情况"""
    return f"{city}{date}的天气是多云转晴"

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

# 将大模型实例绑定工具
llm = llm.bind_tools([get_weather])

# 设置提示词列表
messages = [
    HumanMessage(content="查询北京在2024-12-25日的天气")
]

# 第一次调用llm
result = llm.invoke(messages)

# 将第一次调用llm的结果（工具的选择）添加到提示词列表中
messages.append(result)

# 手动调用工具
tool_info = result.tool_calls[0]
tool_args = tool_info["args"]
tool_id = tool_info["id"]
tool_result = get_weather.invoke(tool_args)

# 将工具调用的信息封装到ToolMessage并追加到messages
messages.append(
    ToolMessage(content=tool_result, tool_call_id=tool_id)
)

# 将messages发送到llm
result = llm.invoke(messages)

print(result)