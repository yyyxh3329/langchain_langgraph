"""
    测试：使用LangChain调用本地工具
"""
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool
def get_weather(city, date):
    """获取某个城市在某天的天气情况"""
    return f"{city}在{date}的天气为 多云转晴"

llm = ChatOpenAI(
    model='gpt-4o-mini'
)

# 将大模型实例绑定工具
llm = llm.bind_tools([get_weather])

# 设置提示词列表
messages = [
    HumanMessage(content="查询上海在2026年-06-15的天气")
]

# 第一次调用llm，此时大模型会进行判断是否调用工具
# 此时返回的是AImessage
result = llm.invoke(messages)
# print(result.tool_calls[0]["name"])
# print(result.tool_calls[0]["args"])

# 将第一次执行的结果添加到 提示词列表中, 里面是工具的选择
messages.append(result)

# 手动的调用工具
tool_result = get_weather.invoke(result.tool_calls[0]["args"])
# 将工具的返回结果封装为ToolMessage
tool_message = ToolMessage(content=tool_result,tool_call_id=result.tool_calls[0]["id"])
# 将工具的返回的AImessage消息添加到提示词列表
messages.append(tool_message)


# 最后将messages发送到大模型
result = llm.invoke(messages)

print(result)