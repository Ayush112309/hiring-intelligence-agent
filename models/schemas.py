# models/schemas.py

from pydantic import BaseModel
from typing import List


class CandidateResult(BaseModel):
    name: str
    match_score: int
    decision: str
    missing_skills: List[str]
    reason: str
    confidence: float
    insight: str
    recommendation: str  


class FinalOutput(BaseModel):
    total_candidates: int
    top_candidate: str | None
    ranking: List[CandidateResult]