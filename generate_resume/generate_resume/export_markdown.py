def save_resume_as_markdown(resume_text: str, filename: str = "resume/resume.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Resume\n\n")
        f.write(resume_text)
