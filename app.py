import streamlit as st
import PyPDF2

# ----------------------------
# Streamlit App UI
# ----------------------------
st.title("AI Resume Analyzer 📄🤖")
st.write("Upload your resume (PDF) and check how well it matches job requirements!")

# File uploader
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Required skills list (you can edit this anytime)
required_skills = ["Python", "Web Development", "Data Science", "Cloud"]

if uploaded_file is not None:
    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Skill Match Results ✅")

    found_skills = []
    missing_skills = []

    # Check skills
    for skill in required_skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    # Show results
    st.success(f"✅ Skills Found: {', '.join(found_skills) if found_skills else 'None'}")
    st.error(f"❌ Missing Skills: {', '.join(missing_skills) if missing_skills else 'None'}")

    # Match Score
    score = (len(found_skills) / len(required_skills)) * 100
    st.subheader(f"📊 Overall Match Score: {score:.2f}%")
