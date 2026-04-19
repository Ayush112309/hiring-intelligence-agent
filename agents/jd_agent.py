# agents/jd_agent.py

def jd_analyzer_agent(jd_text: str):
    jd_text = jd_text.lower()

    skills = ["python", "sql", "excel", "machine learning", "statistics"]

    required = [s.capitalize() for s in skills if s in jd_text]

    return {
        "role": "Data Analyst Intern",
        "required_skills": required,
        "preferred_skills": [],
        "experience_level": "0-2 years"
    }