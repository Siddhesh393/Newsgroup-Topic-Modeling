# 🧠 News Topic Classification App

A **Streamlit-based web application** that predicts the **topic of any given news article or text** using a trained **machine learning pipeline** (Vectorizer + Classifier).  
This project is built on the **20 Newsgroups dataset**, with topics merged into broader categories such as **Technology**, **Science**, **Religion**, **Politics**, **Sports**, and **Vehicles**.

---

## 🚀 Features
- 📰 **Text Classification** — Enter any news text and get its predicted topic.
- ⚡ **Real-Time Prediction** — Interactive Streamlit UI for instant results.
- 💾 **Cached Model Loading** — Faster inference using `@st.cache_resource`.
- 🧩 **Integrated Pipeline** — Vectorization and model inference in one step.
- 🔍 **Label Mapping** — Readable output using a saved LabelEncoder.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.x |
| Framework | Streamlit |
| ML Library | Scikit-learn |
| Serialization | Joblib |
| Dataset | 20 Newsgroups Dataset |

---

## 📂 Project Structure
📦 News_Topic_Classifier
│
├── app.py # Streamlit web app
├── best_text_classifier.pkl # Saved trained ML pipeline
├── label_encoder.pkl # Saved LabelEncoder object
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── data/
└── newsgroups_data.csv # (Optional) Preprocessed dataset


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/News_Topic_Classifier.git
cd News_Topic_Classifier
