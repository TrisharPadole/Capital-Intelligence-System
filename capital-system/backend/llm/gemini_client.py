import google.generativeai as genai
import os
# 🔑 PASTE YOUR GEMINI API KEY HERE
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def call_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
