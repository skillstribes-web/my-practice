import os

from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

sawal = input("Apna sawal likho: ")

jawab = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "Tum ek madadgaar assistant ho. Hamesha Roman Urdu mein jawab do, Hindi mein nahi. Jawab chhota rakho."},
        {"role": "user", "content": sawal},
    ],
    model="openai/gpt-oss-20b",
)

print(jawab.choices[0].message.content)