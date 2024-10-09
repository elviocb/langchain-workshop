# from openai import
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import LLMChain

MemorySaver
from dotenv import load_dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
import langchain

langchain.debug = False

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
    max_tokens=150,
    n=1,
    stop=None,
)

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    chat_memory=FileChatMessageHistory("history.txt"),
)


# memory_summary = ConversationSummaryMemory(
#     memory_key="chat_history",
#     llm=llm,
#     return_messages=True,
# )

chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

# Runnable Sequences (LCEL)
# https://python.langchain.com/docs/concepts/#langchain-expression-language-lcel

# chain = prompt | llm


while True:
    content = input("You: ")

    result = chain.invoke({"content": content})
    print(result["text"])
