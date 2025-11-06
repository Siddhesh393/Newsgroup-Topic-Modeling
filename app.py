import streamlit as st
import joblib

st.set_page_config(page_title="News Topic Classifier", page_icon="📰", layout="centered")

@st.cache_resource
def load_model():
    model = joblib.load("models/final_mnb_pipeline.pkl")  
    label_mapping = joblib.load("data/label_mapping.joblib")
    return model, label_mapping

model, label_mapping = load_model()


st.title("🧠 News Topic Classifier")
st.write("Enter any news article or text below, and the model will predict its category.")


user_input = st.text_area("📝 Paste your text here:", height=200)

if st.button("🔍 Predict Topic"):
    if user_input.strip() == "":
        st.warning("Please enter some text to classify.")
    else:
        
        prediction = model.predict([user_input])[0]
        predicted_label = label_mapping[prediction]

        st.success(f"**Predicted Topic:** {predicted_label}")

        
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba([user_input])[0]
            confidence = max(proba) * 100
            st.write(f"**Confidence:** {confidence:.2f}%")

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and scikit-learn")
