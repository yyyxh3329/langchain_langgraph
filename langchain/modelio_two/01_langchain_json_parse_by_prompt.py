from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class Prime(BaseModel):
    prime: list[int] = Field(description="500以内的所有素数")
    count: int = Field(description="500以内所有素数的个数")


llm = ChatOpenAI(
    model="gpt-4o-mini"
)

json_parse = JsonOutputParser(pydantic_object=Prime)

result = llm.invoke(
    [   ("system",json_parse.get_format_instructions()),
        ("user","生成500以内的所有素数，并给出500以内的所有素数的个数")
    ]
)

# print(json_parse.invoke(result))
# print(result.content)
parsed_res = json_parse.invoke(result)
print(parsed_res)