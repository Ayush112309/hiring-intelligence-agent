# agents/matcher_agent.py

def matcher_agent(jd_data: dict, resume_data: dict):
    jd_required = set(skill.lower() for skill in jd_data.get("required_skills", []))
    resume_skills = set(skill.lower() for skill in resume_data.get("skills", []))

    matched = jd_required.intersection(resume_skills)
    missing = jd_required.difference(resume_skills)

    if len(jd_required) == 0:
        score = 50
    else:
        base_score = (len(matched) / len(jd_required)) * 100
        bonus = len(resume_skills - jd_required) * 5
        score = min(100, int(base_score + bonus))
        # score = int((len(matched) / len(jd_required)) * 100)
        
    return {
        "match_score": score,
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "required_match_count": len(matched),
        "required_total": len(jd_required)
    }