from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

prompt = "Unce upon a time in aland far far away there lived a {character}."

input_variables = {
    "character": "Young lady",
}

formatted_prompt = prompt.format(**input_variables)

response = llm.completions.create(
    model="davinci-002", prompt=formatted_prompt, temperature=0.0, n=1, max_tokens=50
)

generated_text = response.choices[0].text

print("Generated Text:\n")
print(generated_text)
