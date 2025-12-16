import streamlit as st
from resume_parser import extract_text
from keyword_matcher import calculate_match

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
job_keywords_input = st.text_area("Enter Job Keywords (comma-separated)")

if uploaded_file and job_keywords_input:
    resume_text = extract_text(uploaded_file)
    job_keywords = [k.strip() for k in job_keywords_input.split(',')]
    score = calculate_match(resume_text, job_keywords)
    st.success(f"Resume Match Score: {score}%")
