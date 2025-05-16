import streamlit as st
from process_input import process_input, build_structured_data
from generate_sections import generate_resume
from llm_utils import generate_cover_letter
st.set_page_config(page_title="Resume Generator", layout="centered")

st.title("📄 Resume Generator (Qwen-powered)")
input_mode = st.radio("Choose input mode:", ["Freeform (text box)", "Structured (form)"])

if input_mode == "Freeform (text box)":
    user_text = st.text_area("Paste your background description:")
    if st.button("Generate Resume"):
        with st.spinner("Processing..."):
            structured = process_input(user_text)
            resume = generate_resume(structured)
        st.subheader("🎯 Generated Resume")
        st.text(resume)
    if st.button("Generate Cover Letter"):
        job_title = st.text_input("Target Job Title (optional)")
        company = st.text_input("Target Company (optional)")

        with st.spinner("Generating cover letter..."):
            cover_letter = generate_cover_letter(structured, job_title, company)
        st.subheader("📬 Cover Letter")
        st.text(cover_letter)
else:
    with st.form("structured_form"):
        name = st.text_input("Full Name")
        age = st.text_input("Age")
        gender = st.selectbox("Gender", ["", "Male", "Female", "Non-binary", "Other"])
        birthday = st.text_input("Birthday (e.g. May 1, 2001)")
        location = st.text_input("Location")

        degree = st.text_input("Master's Degree")
        major = st.text_input("Master's Major")
        university = st.text_input("Master's University")

        bachelor_degree = st.text_input("Bachelor's Degree")
        bachelor_major = st.text_input("Bachelor's Major")
        bachelor_university = st.text_input("Bachelor's University")

        skills = st.text_area("Skills (comma-separated)")
        experiences = st.text_area("Work Experience (one per line)")
        projects = st.text_area("Projects (one per line)")

        submitted = st.form_submit_button("Generate Resume")
        if submitted:
            form_data = {
                "name": name,
                "age": age,
                "gender": gender,
                "birthday": birthday,
                "location": location,
                "degree": degree,
                "major": major,
                "university": university,
                "bachelor_degree": bachelor_degree,
                "bachelor_major": bachelor_major,
                "bachelor_university": bachelor_university,
                "skills": [s.strip() for s in skills.split(",") if s.strip()],
                "experiences": [e.strip() for e in experiences.split("\n") if e.strip()],
                "projects": [p.strip() for p in projects.split("\n") if p.strip()],
            }

            structured = build_structured_data(form_data)
            resume = generate_resume(structured)
            st.subheader("🎯 Generated Resume")
            st.text(resume)
