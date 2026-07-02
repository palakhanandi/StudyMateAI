import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()
# -----------------------------
# Gemini API Key
# -----------------------------
my_api_key = "YOUR_GEMINI_API"

# Configure Gemini
genai.configure(api_key= my_api_key)
print("API Key =", my_api_key[:10])

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def planner_agent(user_input):
    """
    Generates a personalized study plan.
    """

    prompt = f"""
You are an expert AI Study Planner.

Based on the student's information below, generate a personalized study plan.

Student Details:
{user_input}

Instructions:
1. Create a day-wise timetable.
2. Divide study hours equally.
3. Include short breaks.
4. Include revision days.
5. Prioritize weak subjects.
6. Keep the output neat and easy to read.

Return the answer in Markdown table format.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {e}"
