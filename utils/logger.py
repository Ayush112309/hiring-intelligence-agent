# utils/logger.py

def log_step(step_name: str):
    print(f"\n🔹 {step_name}...\n")


def log_success(message: str):
    print(f"✅ {message}")


def log_error(message: str):
    print(f"❌ {message}")


def log_info(message: str):
    print(f"ℹ️ {message}")