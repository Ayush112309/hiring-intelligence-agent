# agents/resume_agent.py

import re

def extract_name(text: str):
    import re

    lines = text.split("\n")

    invalid_words = {
        "institute", "university", "college", "school",
        "iit", "hyderabad", "engineering", "technology",
        "btech", "degree", "board"
    }

    for line in lines[:10]:
        line = line.strip()

        if not line or "@" in line:
            continue

        clean_line = re.sub(r"[^a-zA-Z\s]", "", line).strip()
        words = clean_line.split()

        if any(w.lower() in invalid_words for w in words):
            continue

        if 2 <= len(words) <= 5 and all(w.isalpha() for w in words):
            return " ".join(words).title()

        if len(words) == 1 and len(words[0]) > 2:
            return words[0].title()

    return "Candidate"

def resume_parser_agent(resume_text: str):
    resume_text_lower = resume_text.lower()

    skills_map = {
        "python": ["python"],
        "sql": ["sql", "mysql"],
        "excel": ["excel"],
        "machine learning": ["machine learning", "ml"],
        "statistics": ["statistics", "statistical", "statistical methods"]
    }

    found_skills = []

    for skill, variants in skills_map.items():
        for v in variants:
            if v in resume_text_lower:
                found_skills.append(skill.capitalize())
                break

    # skills = ["python", "sql", "excel", "machine learning", "c++", "dbms"]
    # found_skills = [s.capitalize() for s in skills if s in resume_text_lower]

    name = extract_name(resume_text)

    return {
        "name": name,
        "skills": found_skills,
        "experience": "Fresher",
        "projects": []
    }
