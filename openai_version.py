from openai import OpenAI
import os

BASE_URL =  "http://localhost:12434/engines/llama.cpp/v1/"
#  v1/chat/completions is not needed in the base URL for OpenAI client 

client = OpenAI(
    base_url = BASE_URL,
    api_key = "anything",)

MODEL_NAME = "ai/smollm2"
PROMPT = "Explain the significance of the theory of relativity in modern physics."


#prepare the chat messages

messages = [
    {        "role": "user",
        "content": PROMPT
    }]

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=messages,)

print("Respones:",response.choices[0].message.content)