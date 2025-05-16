from llm_utils import polish_experience_bullet

if __name__ == "__main__":
    bullet = "Interned at a small startup building dashboards."
    role = "data analyst"
    skills = ["Python", "SQL"]

    print("Sending to Qwen...")
    result = polish_experience_bullet(bullet, role=role, skills=skills)
    print("\n✅ Qwen Output:\n", result)
