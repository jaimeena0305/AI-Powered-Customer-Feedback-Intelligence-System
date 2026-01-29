import streamlit as st
import pandas as pd
import pickle
from llm_utils import classify_complaint, summarize_feedback

# Load ML model
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("🧠 AI Customer Feedback Intelligence System")

df = pd.read_csv("data.csv")

results = []

for review in df["review"]:
    X = vectorizer.transform([review])
    sentiment = model.predict(X)[0]
    sentiment_label = "Positive 😊" if sentiment == 1 else "Negative 😠"

    category = classify_complaint(review)
    results.append([review, sentiment_label, category])

result_df = pd.DataFrame(
    results, columns=["Customer Review", "Sentiment", "Category"]
)

st.subheader("📊 Feedback Analysis")
st.dataframe(result_df)

if st.button("Generate Business Summary"):
    summary = summarize_feedback(df["review"].to_string())
    st.success(summary)
