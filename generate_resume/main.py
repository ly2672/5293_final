from process_input import process_input
from generate_sections import generate_resume
from export_markdown import save_resume_as_markdown
from llm_utils import polish_experience_bullet

def main():
    user_text = input("Please describe your background: ")
    structured_data = process_input(user_text)

    print("\n==================== GENERATED RESUME ====================")
    resume_text = generate_resume(structured_data)
    print(resume_text)

    # Save to Markdown
    save_resume_as_markdown(resume_text)
    print("\n✅ Resume saved as resume.md")

if __name__ == "__main__":
    main()
