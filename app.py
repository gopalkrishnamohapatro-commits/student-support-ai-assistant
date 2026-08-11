import streamlit as st
import json
import random
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Support AI Assistant",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# Load Intents
# -----------------------------
def load_intents():
    file_path = "intents.json"

    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return {"intents": []}

    return {"intents": []}


data = load_intents()
intents = data.get("intents", [])

# -----------------------------
# Internship Dataset
# -----------------------------
internships = [
    {
        "title": "AI & Machine Learning Internship",
        "skills": ["python", "machine learning", "pandas", "scikit-learn"],
        "domain": "Artificial Intelligence"
    },
    {
        "title": "Data Science Internship",
        "skills": ["python", "pandas", "numpy", "data analysis"],
        "domain": "Data Science"
    },
    {
        "title": "NLP Internship",
        "skills": ["python", "nlp", "natural language processing"],
        "domain": "Natural Language Processing"
    },
    {
        "title": "Computer Vision Internship",
        "skills": ["python", "opencv", "computer vision"],
        "domain": "Computer Vision"
    },
    {
        "title": "Python Development Internship",
        "skills": ["python", "programming", "sql"],
        "domain": "Python Development"
    }
]

# -----------------------------
# Chatbot Response Function
# -----------------------------
def get_response(user_message):
    message = user_message.lower()

    for intent in intents:
        patterns = intent.get("patterns", [])
        responses = intent.get("responses", [])

        for pattern in patterns:
            if pattern.lower() in message:
                if responses:
                    return random.choice(responses)

    # Basic fallback responses
    if "internship" in message:
        return (
            "I can help you find suitable internships. "
            "Tell me your skills, such as Python, Machine Learning, "
            "Data Science or NLP."
        )

    if "hello" in message or "hi" in message:
        return "Hello! 👋 I am your Student Support AI Assistant."

    if "help" in message:
        return (
            "I can help with student support, internships, "
            "skills and internship recommendations."
        )

    return (
        "Sorry, I could not understand that. "
        "Please ask about internships, skills or student support."
    )


# -----------------------------
# Recommendation Engine
# -----------------------------
def recommend_internships(skills):
    user_skills = [
        skill.strip().lower()
        for skill in skills.split(",")
        if skill.strip()
    ]

    results = []

    for internship in internships:
        matched_skills = []

        for skill in user_skills:
            for required_skill in internship["skills"]:
                if skill in required_skill or required_skill in skill:
                    matched_skills.append(required_skill)

        if matched_skills:
            score = len(set(matched_skills))

            results.append({
                "title": internship["title"],
                "domain": internship["domain"],
                "score": score,
                "matched": list(set(matched_skills))
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results


# -----------------------------
# Application UI
# -----------------------------
st.title("🎓 Student Support AI Assistant")

st.write(
    "AI-powered Student Support and Internship Management Assistant "
    "using NLP and Machine Learning."
)

st.divider()

# -----------------------------
# Internship Recommendation
# -----------------------------
st.header("💼 Internship Recommendation Engine")

st.write(
    "Enter your skills separated by commas to get suitable internship recommendations."
)

skills = st.text_input(
    "Your Skills",
    placeholder="Example: Python, Machine Learning, Pandas"
