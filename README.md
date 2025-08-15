## 📜 Resume Shortlisting Predictor

<img width="1140" height="633" alt="Screenshot 2025-08-15 185952" src="https://github.com/user-attachments/assets/996d926d-ae81-4b3f-929e-e27d2d741fcd" />

<img width="1126" height="630" alt="Screenshot 2025-08-15 185855" src="https://github.com/user-attachments/assets/b8ff4e00-7e18-48e3-9830-bc06f00c498d" />

The **Resume Shortlisting Predictor** is a machine learning-based Streamlit web app that analyzes resumes and predicts whether they are likely to be shortlisted.  
It allows users to **upload their resume** or **paste the text** for instant predictions, helping job seekers optimize their resumes for better chances.

---

## 🚀 Features

- **Resume Upload** – Upload `.txt`, `.docx`, or `.pdf` resumes for analysis.  
- **Text Input** – Paste your resume text directly into the app.  
- **Machine Learning Predictions** – Uses a trained ML model to classify resumes as *Shortlisted* or *Rejected*.  
- **Beautiful UI** – Custom gradient background, styled upload box, and clean typography.  
- **Fast & Easy** – Instant predictions with just a click.  

---

## 🛠️ Tech Stack

- **Frontend & Deployment**: [Streamlit](https://streamlit.io/)  
- **Backend & ML**: Python, scikit-learn, pandas, numpy  
- **File Handling**: joblib, nltk  
- **Styling**: Custom CSS for Streamlit  

---

## 📂 Project Structure
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies for deployment
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF Vectorizer
├── encoder.pkl # Label Encoder
├── README.md # Project documentation
└── assets/ # (Optional) Images, icons, styles

---

## 📜 License
This project is licensed under the **Apache 2.0** – you are free to use and modify it.

---

## 🙌 Acknowledgments
Special thanks to open-source communities and Python libraries that made this project possible.
