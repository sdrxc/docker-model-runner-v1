import requests

url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"
# As its a request, it require the v1/chat/completions in the base URL

data = {
    "model": "ai/smollm2",
    "messages": [
        {
            "role": "user",
            "content": "What is the capital of France?"
        },
        {
            "role": "system",
            "content": "Please write a 500-word essay on the impact of climate change on global agriculture."
        }
    ]
}

response = requests.post(url, json=data, verify=False)
response.raise_for_status()  # Raise an error for bad responses
print("Response Status Code:", response.status_code)
# Print the response content
print("Response json:", response.json())
# Extract and print the content of the response
print(response.json()["choices"][0]["message"]["content"]) 
