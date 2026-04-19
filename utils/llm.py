# utils/llm.py

import os
from dotenv import load_dotenv

load_dotenv()

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    USE_LLM = True if os.getenv("OPENAI_API_KEY") else False
except:
    USE_LLM = False


def call_llm(prompt: str, temperature: float = 0.2, model: str = "gpt-4o-mini"):
    if not USE_LLM:
        return fallback_response(prompt)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )

        content = response.choices[0].message.content

        if not content:
            return "ERROR: Empty LLM response"

        return content.strip()

    except Exception as e:
        print(f"⚠️ LLM Error: {e}")
        return fallback_response(prompt)

def fallback_response(prompt: str):

    prompt = prompt.lower()

    if "job description" in prompt:
        return """{
            "role": "Data Analyst Intern",
            "required_skills": ["python", "sql", "statistics", "excel"],
            "preferred_skills": [],
            "experience_level": "0-2 years"
        }"""

    if "resume" in prompt:
        return """{
            "name": "Candidate",
            "skills": ["python", "sql"],
            "experience": "Fresher",
            "projects": []
        }"""

    if "decision" in prompt:
        return """{
            "decision": "Consider",
            "confidence": 0.7,
            "reason": "Basic match found"
        }"""

    return "Fallback response"
