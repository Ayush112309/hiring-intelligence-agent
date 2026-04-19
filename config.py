# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# LLM Config
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.2))

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
JD_PATH = os.path.join(DATA_DIR, "sample_jd.txt")
RESUME_FOLDER = os.path.join(DATA_DIR, "sample_resumes")

# Limits (Optional but Smart)
MAX_TEXT_LENGTH = 4000