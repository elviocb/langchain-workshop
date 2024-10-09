# from openai import
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
    max_tokens=150,
    n=1,
    stop=None,
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(
        content="Can you provide a nodejs function that returns a list from 0 to 10"
    ),
]

ai_reply = llm.invoke(messages)

print("(AI reply):\n")
print(ai_reply.content)
