import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('punkt')

def analyze_resume(resume_text, job_description):
    vectorizer = CountVectorizer().fit_transform([resume_text, job_description])
    similarity = cosine_similarity(vectorizer)[0][1]
    return round(similarity * 100, 2)

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠")
st.title("🧠 AI Resume Analyzer")

st.markdown("Compare your resume with a job description and get a match score using NLP.")

resume_input = st.text_area("📄 Paste your resume text here")
job_input = st.text_area("📝 Paste the job description here")

if st.button("🔍 Analyze"):
    if resume_input and job_input:
        score = analyze_resume(resume_input, job_input)
        st.success(f"✅ Match Score: {score}%")
        if score > 75:
            st.info("Great match! Your resume aligns well with the job description.")
        elif score > 50:
            st.warning("Decent match. Consider tailoring your resume more closely.")
        else:
            st.error("Low match. Try revising your resume to better reflect the job requirements.")
    else:
        st.warning("Please enter both resume and job description.")
