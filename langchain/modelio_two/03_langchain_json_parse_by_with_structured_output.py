"""
    以后基本上用的都是这个方法
"""

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class Prime(BaseModel):
    prime: list[int] = Field(description="500以内的所有素数")
    count: int = Field(description="500以内所有素数的个数")


llm = ChatOpenAI(
    model="gpt-4o-mini"
)

parse_llm = llm.with_structured_output(schema=Prime)


result = parse_llm.invoke(
    [
        ("user","生成500以内的所有素数，并给出500以内的所有素数的个数")
    ]
)

print(result)
