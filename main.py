# main.py

import os

# Config
from config import JD_PATH, RESUME_FOLDER, MAX_TEXT_LENGTH

# Agents
from agents.planner_agent import planner_agent
from agents.jd_agent import jd_analyzer_agent
from agents.resume_agent import resume_parser_agent
from agents.matcher_agent import matcher_agent
from agents.decision_agent import decision_agent

# Tools
from tools.pdf_parser import load_pdf_text
from tools.text_cleaner import clean_text

# Utils
from utils.logger import log_step, log_success, log_error, log_info

# Models
from models.schemas import CandidateResult, FinalOutput


def load_text_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        log_error(f"Error reading file: {e}")
        return ""


def run_pipeline(jd_path: str, resumes_folder: str):
    print("\n🚀 Starting Hiring Intelligence Pipeline...\n")

    # Step 1: Load Job Description
    log_step("Loading Job Description")

    jd_raw = load_text_file(jd_path)
    if not jd_raw:
        log_error("Job Description is empty or not found.")
        return {}

    jd_text = clean_text(jd_raw)[:MAX_TEXT_LENGTH]
    log_success("Job Description Loaded")

    # Step 2: Planner Agent
    log_step("Running Planner Agent")

    plan = planner_agent(jd_text)
    log_info(f"Plan: {plan}")

    # Step 3: JD Analyzer
    log_step("Analyzing Job Description")

    jd_data = jd_analyzer_agent(jd_text)
    log_success("JD Analysis Complete")

    results = []

    # Step 4: Process Resumes
    log_step("Processing Resumes")

    for file in os.listdir(resumes_folder):
        if not file.endswith(".pdf"):
            continue

        print("\n--------------------------------------------------")
        log_step(f"Processing Resume: {file}")

        resume_path = os.path.join(resumes_folder, file)

        resume_raw = load_pdf_text(resume_path)
        resume_text = clean_text(resume_raw)[:MAX_TEXT_LENGTH]

        if not resume_text.strip():
            log_error("Empty resume, skipping...")
            continue

        resume_data = resume_parser_agent(resume_raw)
        match_data = matcher_agent(jd_data, resume_data)
        decision = decision_agent(match_data)

        candidate = CandidateResult(
            name=resume_data.get("name", file),
            match_score=match_data.get("match_score", 0),
            decision=decision.get("decision", "Unknown"),
            missing_skills=match_data.get("missing_skills", []),
            reason=decision.get("reason", ""),
            confidence=decision.get("confidence", 0.0),
            insight=decision.get("insight", ""),
            recommendation=decision.get("recommendation", "")
        )

        results.append(candidate)
        log_success(f"Processed {candidate.name}")

    # Step 5: Ranking (SMART)
    log_step("Ranking Candidates")

    priority = {"Shortlist": 3, "Consider": 2, "Reject": 1}

    ranked = sorted(
        results,
        key=lambda x: (priority.get(x.decision, 0), x.match_score),
        reverse=True
    )

    # Display Results
    print("\n🏆 Final Ranking:\n")

    for i, c in enumerate(ranked, 1):
        print(f"{i}. {c.name}")
        print(f"   Score: {c.match_score}% | Decision: {c.decision} | Confidence: {c.confidence}")
        print(f"   Missing Skills: {c.missing_skills}")
        print(f"   Insight: {c.insight}")
        print(f"   Recommendation: {c.recommendation}")
        print()

    # Top Candidate Summary
    if ranked:
        top = ranked[0]
        print("⭐ TOP CANDIDATE SUMMARY")
        print(f"Name: {top.name}")
        print(f"Score: {top.match_score}%")
        print(f"Why: {top.insight}")
        print()

    # Summary Section
    shortlisted = [c.name for c in ranked if c.decision == "Shortlist"]
    considered = [c.name for c in ranked if c.decision == "Consider"]
    rejected = [c.name for c in ranked if c.decision == "Reject"]

    print("📊 SUMMARY")
    print(f"Shortlisted: {shortlisted}")
    print(f"Consider: {considered}")
    print(f"Rejected: {rejected}")

    # Final Output
    final_output = FinalOutput(
        total_candidates=len(ranked),
        top_candidate=ranked[0].name if ranked else None,
        ranking=ranked
    )

    return final_output


if __name__ == "__main__":
    result = run_pipeline(JD_PATH, RESUME_FOLDER)

    print("\n📦 Final Structured Output:\n")
    print(result.model_dump())