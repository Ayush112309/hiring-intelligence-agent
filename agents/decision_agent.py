# agents/decision_agent.py
def decision_agent(match_data: dict):
    score = match_data.get("match_score", 0)
    matched = match_data.get("matched_skills", [])
    missing = match_data.get("missing_skills", [])

    if score >= 70:
        decision = "Shortlist"
        confidence = 0.9
    elif score >= 40:
        decision = "Consider"
        confidence = 0.75
    else:
        decision = "Reject"
        confidence = 0.6

    # Insight
    insight = (
        f"{len(matched)}/{len(matched)+len(missing)} required skills matched. "
        f"Matched: {matched}. Missing: {missing}."
    )

    # Recommendation
    if decision == "Shortlist":
        recommendation = "Proceed to interview"
    elif decision == "Consider":
        recommendation = f"Improve skills in: {missing[:2]}"
    else:
        recommendation = f"Needs improvement in: {missing}"

    return {
        "decision": decision,
        "reason": "Skill-based evaluation",
        "confidence": confidence,
        "insight": insight,
        "recommendation": recommendation
    }