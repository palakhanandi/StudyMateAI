import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def quiz_agent(user_input):

    prompt = f"""
You are a Quiz Generator AI.

Create 5 MCQs on:

{user_input}

Rules:

- Four options each
- Mention correct answer
- Number questions
"""

    response = model.generate_content(prompt)

    return response.text