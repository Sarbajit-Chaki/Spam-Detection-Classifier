import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load(open('spam_model.pkl', 'rb'))
vectorizer = joblib.load(open('vectorizer.pkl', 'rb'))

# Predict function
def predictMessage(message):
    messageVector = vectorizer.transform([message])
    prediction = model.predict(messageVector)
    return 'Spam' if prediction[0] == 1 else 'Ham'



# Page setup
st.set_page_config(page_title="Spam Detection System", page_icon="🚫", layout="centered")

# Main container
st.markdown('<div style="font-size: 2.5rem; margin-left:-7px; margin-bottom:20px; font-weight: bold;">📩 Spam Detection Classifier</div>', unsafe_allow_html=True)

# Input
message = st.text_area('message', placeholder='Enter your message...', label_visibility='collapsed', height=120)

# Button
if st.button("Predict"):
    if not message.strip():
        st.warning("⚠️ Please enter a message before detection.")
    elif len(message) < 8:
        st.warning("⚠️ Message is too short for detection.")
    else:
        result = predictMessage(message)
        color = "#ef4444" if result == "Spam" else "#22c55e"
        st.markdown(
            f'<div style="text-align: center; font-weight: bold; font-size: 20px; border-radius: 5px; padding: 4px 0px; background-color:{color}; color:white;">{result}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)