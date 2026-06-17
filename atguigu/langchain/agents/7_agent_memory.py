"""
    测试：使用Agent实现短期记忆功能
    1、使用InMemorySaver创建检查点实例，在创建智能体时，设置参数checkpointer=InMemorySaver实例
    2、调用模型时，在设置提示词的同时，也需要设置config={"configurable":{"thread_id":"xxx"}}，
    此时，agent就会将thread_id相同的这些对话记录到同一个消息列表中
"""
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

# 创建检查点实例
checkpointer = InMemorySaver()

agent = create_agent(
    model=llm,
    checkpointer=checkpointer,
)

result = agent.invoke(
    input={
        "messages":[
            ("user", "什么是LangGraph")
        ]
    },
    config={"configurable":{"thread_id":"abc123"}}
)

print(result)

result = agent.invoke(
    input={
        "messages":[
            ("user", "我刚才问了什么")
        ]
    },
    config={"configurable":{"thread_id":"abc123"}}
)

print(result)