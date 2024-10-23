from openai import OpenAI
secret_key="-----"
prompt = "Give me a summary"

client = OpenAI (
    api_key=secret_key,
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
    max_tokens=1000,
    temperature=0
)

print(completion)