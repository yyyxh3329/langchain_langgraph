from openai import OpenAI
from pydantic import BaseModel


def openai_json_output_demo():
    client = OpenAI()

    class CalendarEvent(BaseModel):
        name: str
        date: str
        participants: list[str]

    response = client.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Alice and Bob are going to a science fair on Friday.",
            }
        ],
        response_format=CalendarEvent
    )

    print(response.choices[0].message.parsed)


if __name__ == '__main__':
    openai_json_output_demo()
