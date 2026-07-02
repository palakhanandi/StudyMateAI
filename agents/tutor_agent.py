import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = "AQ.Ab8RN6Iy8miq4fBCFVvKUHjYphX03rRi1BNryyqsUa3cOh8DEw"

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")



model = genai.GenerativeModel("gemini-2.5-flash")

def tutor_agent(user_input):

    prompt = f"""
You are an expert tutor.

Explain the following topic in simple language.

Topic:
{user_input}

Rules:
- Explain step by step.
- Use examples.
- Keep language easy.
- Mention important points.
"""

    response = model.generate_content(prompt)

    return response.text