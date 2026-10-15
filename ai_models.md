# openapi

```python

url = "https://api.openai.com/v1/chat/completions"

api_key = os.getenv("OPENAI_API_KEY")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

body = {
    "model": "gpt-6-luna",
    "messages": [
        {"role": "system", "content": "You are MakeMyTrip's friendly travel assistant. Answer in 2 short lines."},
        {"role": "user", "content": "I'm going to vietnam this weekend (1 october 2026). What should I pack?"},
    ],
}

response = requests.post(url, headers=headers, json=body, timeout=60)
data = response.json()
print(data['choices'][0]['message']['content'])

```

* using direct api:

```python

from openai import OpenAI

client = OpenAI(api_key=api_key)                     # reads OPENAI_API_KEY automatically

response = client.chat.completions.create(
    model="gpt-6-astra",
    response_format={"type":"json_object"},  ## forces valid JSON
    messages=[
        {"role": "system", "content": "You are MakeMyTrip's friendly travel assistant. Answer in 2 short lines."},
        {"role": "user", "content": "I'm going to Goa this weekend. What should I pack?"},
    ],
)

print(response.choices[0].message.content)
```

* groq.com

url: https://console.groq.com/keys

```python
client = OpenAI(api_key=groq_api_key, baseurl="https://api.groq.com/openai/v1")
model = "openai/gpt-oss-20b"



```
