# from openai import OpenAI
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()

llm = OpenAI(model_name="davinci-002", temperature=0.0, max_tokens=50)

prompt = PromptTemplate(
    template="Unce upon a time in aland far far away there lived a {character}.",
    input_variables=["character"],
)

input_variables = {
    "character": "Young lady",
}

formatted_prompt = prompt.format(**input_variables)

response = llm.invoke(formatted_prompt)

generated_text = response

print("Generated Text:\n")
print(generated_text)
