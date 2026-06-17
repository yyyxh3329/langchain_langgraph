"""
    测试：节点的缓存
"""
import time
from typing import TypedDict

from langgraph.cache.memory import InMemoryCache
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.constants import END, START
from langgraph.graph import StateGraph
from langgraph.types import CachePolicy


class MyState(TypedDict):
    x: int
    result: int


def node_cache(state: MyState):
    print("node_cache开始执行")
    time.sleep(2)
    print("node_cache执行完毕")
    return {"result": state["x"] * 2}


checkpointer = InMemorySaver()
builder = StateGraph(MyState)

# 在添加节点时，设置节点的缓存策略
builder.add_node(node_cache, cache_policy=CachePolicy(ttl=5))

builder.add_edge(START, "node_cache")
builder.add_edge("node_cache", END)

graph = builder.compile(checkpointer=checkpointer, cache=InMemoryCache())
# graph = builder.compile(cache=InMemoryCache())

# 节点缓存 存入的是键值对结构，其中的键为 pickle对输入进行hash运算的结果，也就是对x=5进行hash运算，如果x!=5 则不会触发缓存
result = graph.invoke({"x": 5}, config={"configurable": {"thread_id": "1"}})
print(result)

time.sleep(3)

result = graph.invoke({"x": 5}, config={"configurable": {"thread_id": "2"}})
print(result)

# 在节点缓存中使用checkpoint的区别
# 1. 没有 Checkpoint 时
# 每次调用都是独立的：没有状态保存
# 节点缓存生效：相同的输入会命中缓存
# 不需要 thread_id：因为没有状态需要区分
#
# 2. 有 Checkpoint 时
# 状态被持久化：相同的 thread_id 会恢复状态
# Checkpoint 优先：比节点缓存优先级更高
# 需要不同的 thread_id：才能看到节点缓存的效果
# 关键点：节点缓存的键包含节点名称和输入状态的哈希，但不包含 thread_id。所以理论上，不同的 thread_id 如果输入相同能命中缓存