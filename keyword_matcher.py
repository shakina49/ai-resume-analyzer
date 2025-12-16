def calculate_match(resume_text, job_keywords):
    resume_words = set(resume_text.lower().split())
    job_keywords_set = set([k.lower() for k in job_keywords])
    matched_keywords = resume_words.intersection(job_keywords_set)
    score = (len(matched_keywords) / len(job_keywords_set)) * 100
    return round(score, 2)
