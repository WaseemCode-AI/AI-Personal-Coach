import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API Key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = input("Kuch poochho: ")
    print("🤖 AI: ", chat_with_ai(user_input))
