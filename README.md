```markdown
# 🤖 Hiring Intelligence Agent

## 🚀 Problem Statement

Recruiters often spend significant time manually screening resumes against job descriptions. This process is:

- Time-consuming  
- Subjective  
- Difficult to scale  

There is a need for an automated system that can:

- Analyze job requirements  
- Evaluate multiple resumes  
- Rank candidates objectively  
- Provide clear reasoning for decisions  

---

## 💡 Solution

This project presents a **Hiring Intelligence Agent**, a multi-agent system that:

- Parses job descriptions and resumes  
- Matches candidates based on required skills  
- Generates structured hiring decisions  
- Provides explainable insights and recommendations  

The system simulates a real-world hiring pipeline using an **agentic workflow**, where each agent performs a specialized task.

---

## 🧠 Architecture

The system is designed as a **multi-agent workflow**, where each agent performs a specific role.

### 🔄 Workflow Overview

```

User Input (JD + Resumes)
↓
Planner Agent
↓
JD Analyzer Agent
↓
Resume Parser Agent
↓
Matcher Agent
↓
Decision Agent
↓
Ranking & Output

````

---

### 🤖 Agents

**1. Planner Agent**
- Defines execution flow

**2. JD Analyzer Agent**
- Extracts required skills

**3. Resume Parser Agent**
- Extracts name + skills from PDFs  
- Handles noisy data  

**4. Matcher Agent**
- Computes match score  
- Identifies matched & missing skills  

**5. Decision Agent**
- Outputs:
  - Decision (Shortlist / Consider / Reject)  
  - Confidence score  
  - Insights  
  - Recommendations  

---

### 📦 Structured Output

- Implemented using **Pydantic**
- Ensures consistent JSON outputs
- Improves reliability

---

### ⚙️ Design Highlights

- Modular agent-based system  
- Explainable decision-making  
- Semantic skill matching  
- Robust PDF parsing  

---

## ⚙️ How to Run

### 1. Clone Repo

```bash
git clone <your-repo-link>
cd hiring-agent
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Data

Place resumes in:

```
data/sample_resumes/
```

Update job description:

```
data/sample_jd.txt
```

### 4. Run

```bash
python main.py
```

---

## 📊 Example Output

```
🏆 Final Ranking:

1. Sneha Iyer
   Score: 100% | Decision: Shortlist | Confidence: 0.9
   Missing Skills: []
   Insight: 4/4 required skills matched. Matched: ['statistics', 'excel', 'python', 'sql']. Missing: [].
   Recommendation: Proceed to interview

2. Rohan Mehta
   Score: 55% | Decision: Consider | Confidence: 0.75
   Missing Skills: ['statistics', 'excel']
   Insight: 2/4 required skills matched. Matched: ['python', 'sql']. Missing: ['statistics', 'excel'].
   Recommendation: Improve skills in: ['statistics', 'excel']

3. Amit Verma
   Score: 0% | Decision: Reject | Confidence: 0.6
   Missing Skills: ['statistics', 'excel', 'python', 'sql']
   Insight: 0/4 required skills matched. Matched: []. Missing: ['statistics', 'excel', 'python', 'sql'].
   Recommendation: Needs improvement in: ['statistics', 'excel', 'python', 'sql']

⭐ TOP CANDIDATE SUMMARY
Name: Sneha Iyer
Score: 100%
Why: 4/4 required skills matched. Matched: ['statistics', 'excel', 'python', 'sql']. Missing: [].

📊 SUMMARY
Shortlisted: ['Sneha Iyer']
Consider: ['Rohan Mehta']
Rejected: ['Amit Verma']
```

---

## 🔮 Future Improvements

* LLM-based reasoning
* Semantic embeddings for skill matching
* Weighted scoring system
* Better resume parsing (experience/projects)
* LangGraph-based workflow
* UI dashboard for recruiters
* Database integration
* Bias & fairness improvements

---

## 🎯 Summary

This project demonstrates how **agentic workflows** can automate real-world decision systems like hiring.

It combines:

* Multi-agent architecture
* Structured outputs
* Explainable reasoning

to create a scalable hiring intelligence system.

```