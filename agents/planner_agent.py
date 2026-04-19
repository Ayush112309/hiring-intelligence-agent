# agents/planner_agent.py

def planner_agent(jd_text: str):
    """
    Defines the workflow steps dynamically (simple but useful for demo).
    """

    return {
        "steps": [
            "Analyze Job Description",
            "Parse Resumes",
            "Match Candidates",
            "Make Hiring Decision",
            "Rank Candidates"
        ],
        "reason": "Standard multi-step hiring pipeline based on job description analysis"
    }