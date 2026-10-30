import os

from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

jawab = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Ek line mein batao ke Python kya hai. Jawab Roman Urdu mein do, Hindi mein nahi."}
    ],
    model="openai/gpt-oss-20b",
)

print(jawab.choices[0].message.content)