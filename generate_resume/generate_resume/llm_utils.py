import os
from dotenv import load_dotenv
from openai import OpenAI
import re
# Load the .env file
load_dotenv()

# Get raw key from .env
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise ValueError("❌ API key not found in .env file!")

# ✅ DO NOT add "Bearer " prefix manually — DashScope doesn't want it
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # ✅ correct
)

def polish_experience_bullet(bullet, role=None, skills=None):
    prompt = f"""Expand the following experience into 3–4 well-written resume bullet points. Each bullet should be specific and professionally written.

Original: "{bullet}"
"""

    if role:
        prompt += f"\nTarget role: {role}"
    if skills:
        prompt += f"\nRelevant skills: {', '.join(skills)}"

    try:
        response = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {"role": "system", "content": "You are a helpful resume assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ Error communicating with Qwen:", str(e))
        return bullet


def polish_skills(skills):
    if not skills:
        return "No skills provided."

    prompt = f"""
Polish and format the following list of skills to make it look professional in a resume. Group them logically and rewrite technical acronyms if needed.
Skills: {', '.join(skills)}
"""

    try:
        response = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ Error polishing skills:", str(e))
        return ", ".join(skills)
    
def clean_resume_text(text):
    # Remove "Original / Revised" and following content
    text = re.sub(r"\*\*Original:\*\*.*?\n", "", text, flags=re.DOTALL)
    text = re.sub(r"\*\*Revised:\*\*\s*", "", text, flags=re.DOTALL)
    
    # Remove markdown-style headings
    #text = re.sub(r"^#{1,6} .*", "", text, flags=re.MULTILINE)
    
    # Remove "Why This Works" section and anything after
    text = re.split(r"(### Why This Works|## Explanation|---)", text)[0]

    # Remove triple dashes
    text = text.replace("---", "")

    return text.strip()

def generate_cover_letter(data, job_title=None, company=None):
    prompt = f"""Write a professional and concise cover letter in 3 paragraphs for a job application."""

    if data.get("name"):
        prompt += f"\nThe applicant's name is {data['name']}."
    if job_title:
        prompt += f"\nThe job title is {job_title}."
    if company:
        prompt += f"\nThe company is {company}."

    # Summary of resume
    if data.get("degree") or data.get("major"):
        prompt += f"\nThe applicant is a student in {data.get('major', '')} with a {data.get('degree', '')}."
    if data.get("experiences"):
        prompt += f"\nThey have experience such as: {', '.join(data['experiences'][:2])}."
    if data.get("skills"):
        prompt += f"\nTheir skills include: {', '.join(data['skills'])}."

    prompt += "\nMake it formal, enthusiastic, and specific to the job."

    try:
        response = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {"role": "system", "content": "You are a helpful resume and cover letter assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ Error generating cover letter:", str(e))
        return "Cover letter could not be generated."
