from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

prompt = "Unce upon a time in aland far far away there lived a {character}."

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": "Can you provide a nodejs function that returns a list from 0 to 10",
    },
]


response = llm.chat.completions.create(
    model="gpt-4o", messages=messages, temperature=0.0, n=1, max_tokens=150
)

ai_reply = response.choices[0].message.content

print("(AI reply):\n")
print(ai_reply)
