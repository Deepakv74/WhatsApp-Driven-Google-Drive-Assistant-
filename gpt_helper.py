import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    prompt = f"Summarize the following in bullet points:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=400
    )
    return response['choices'][0]['message']['content']
