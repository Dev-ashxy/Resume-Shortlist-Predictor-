import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

# Ensure NLTK stopwords are downloaded
nltk.download('stopwords')

# ---------- Load Model and Vectorizer ----------
@st.cache_resource
def load_model():
    model = joblib.load("resume_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# ---------- Preprocessing Function ----------
def clean_resume(resume_text):
    resume_text = re.sub('http\\S+\\s*', ' ', resume_text)  # Remove URLs
    resume_text = re.sub('RT|cc', ' ', resume_text)  # Remove RT and cc
    resume_text = re.sub('#\\S+', '', resume_text)  # Remove hashtags
    resume_text = re.sub('@\\S+', ' ', resume_text)  # Remove mentions
    resume_text = re.sub('[^A-Za-z ]+', ' ', resume_text)  # Keep only letters
    resume_text = resume_text.lower()  # Lowercase
    tokens = resume_text.split()
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return " ".join(tokens)


st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background: linear-gradient(90deg, #C5ADC5, #B2B5E0); /* Pastel Purple to Light Steel Blue */
    }

    /* File upload box deep gray */
    .stFileUploader {
        background-color: #4B4B4B !important; /* Deep Gray */
        border-radius: 10px;
        padding: 10px;
    }

    /* Make text inside upload box white for contrast */
    .stFileUploader label, .stFileUploader div {
        color: white !important;
    }

    /* Change textarea and other input text to black */
    textarea, input, .stTextArea textarea, .stTextInput input {
        color: lavender !important;
    }

    /* Heading style */
    h1 {
        color: #4B1C4B !important; /* Deep Charcoal */
        font-weight: bold;
    }
    label, .stTextArea label, .stFileUploader label {
        color: #5D3A66 !important; /* Rich Plum */
        font-weight: bold;
    }
     .stMarkdown p {
        color: #8E4585 !important; /* Rich Plum */
    }
    </style>
    """,
    unsafe_allow_html=True
)





# ---------- Streamlit UI ----------
st.title("📒 Resume Shortlisting Predictor")
st.write("📜 Upload your resume or paste the text below to predict whether it will be shortlisted.")

# Text input
resume_input = st.text_area("📝 Paste Resume Text Here", height=150)

# File upload option
uploaded_file = st.file_uploader("📂 Or upload a .txt .pdf .docx file", type=["txt", "docx", "pdf"])
if uploaded_file is not None:
    resume_input = uploaded_file.read().decode("utf-8", errors="ignore")

# Prediction
if st.button("🔍 Predict"):
    if resume_input.strip() == "":
        st.warning("⚠ Please provide some resume text.")
    else:
        cleaned = clean_resume(resume_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        prediction_proba = model.predict_proba(vectorized)[0]

        st.subheader("Prediction Result:")
        st.write(f"**Status:** {'✅ Shortlisted' if prediction == 1 else '❌ Rejected'}")
        st.write(f"**Probability of Shortlist:** {prediction_proba[1]*100:.2f}%")

        st.progress(float(prediction_proba[1]))

st.markdown("---")
st.caption("✨Powered by Streamlit & Scikit-learn")



