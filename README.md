# 🧠 AI-Powered Customer Feedback Intelligence System

## 📌 Overview
This project is an end-to-end **AI-powered analytics system** that analyzes large volumes of customer feedback using **Machine Learning and Generative AI**.  
It automatically identifies customer sentiment, categorizes complaints, and generates business-friendly summaries to support data-driven decision making.

The system is designed to simulate how modern analytics teams use **AI-assisted workflows** to extract insights from unstructured text data.

---

## 🎯 Problem Statement
Organizations receive thousands of customer reviews and support messages daily.  
Manually analyzing this unstructured feedback is time-consuming and inefficient.

**Goal:**  
Build an automated system that:
- Understands customer feedback
- Identifies sentiment (positive/negative)
- Categorizes complaints (delivery, refund, product quality, support)
- Generates executive-level insight summaries

---

## 🧩 Solution Architecture

Customer Feedback (Text)
↓
Machine Learning (Sentiment Analysis)
↓
Prompt-Engineered LLM (Complaint Categorization)
↓
AI-Generated Business Summary
↓
Interactive Dashboard (Streamlit)


This workflow functions as an **AI-driven feedback analysis agent**.

---

## 🛠️ Tech Stack

| Category | Tools |
|--------|------|
| Programming | Python |
| Data Handling | Pandas |
| Machine Learning | Scikit-learn (TF-IDF, Logistic Regression) |
| Generative AI | OpenAI API (LLMs) |
| Prompt Engineering | Custom task-specific prompts |
| Visualization | Streamlit |
| Version Control | Git & GitHub |

---

## 📊 Dataset
- **2,000+ realistic customer reviews**
- Automatically generated using Python
- Mix of positive and negative feedback
- Covers delivery, refund, product quality, and customer support issues

---

## ⚙️ Key Features

### ✅ Sentiment Analysis (Machine Learning)
- Uses TF-IDF vectorization
- Logistic Regression classifier
- Classifies feedback as **Positive** or **Negative**

### ✅ Complaint Categorization (Generative AI)
- Uses prompt-engineered LLM workflows
- Automatically tags reviews into business categories

### ✅ AI-Generated Business Insights
- Summarizes large volumes of feedback
- Highlights major issues and customer satisfaction trends

### ✅ Interactive Dashboard
- Displays analyzed feedback
- One-click generation of executive summaries

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install pandas scikit-learn streamlit openai

2️⃣ Generate Dataset
python generate_data.py

3️⃣ Train ML Model
python ml_model.py

4️⃣ Run the Application
streamlit run app.py

📁 Project Structure
ai-customer-feedback/
│
├── app.py                  # Streamlit dashboard
├── data.csv                # Customer feedback dataset
├── generate_data.py        # Realistic data generator
├── ml_model.py             # ML sentiment model training
├── llm_utils.py            # Prompt-engineered LLM functions
├── sentiment_model.pkl     # Trained ML model
├── vectorizer.pkl          # TF-IDF vectorizer
├── README.md
└── requirements.txt

📈 Business Impact

Reduces manual feedback analysis effort

Enables faster issue identification

Helps teams prioritize customer pain points

Demonstrates real-world AI-assisted analytics workflows

🚀 Future Enhancements

Store feedback and results in SQL database

Add trend analysis over time

Deploy as a web service

Integrate automated weekly reporting agent

👤 Author

Jai Meena
Skills: Python, SQL, Machine Learning, AI & Analytics

⭐ Why This Project Matters

This project demonstrates applied AI, not just model building.
It shows how Machine Learning and Generative AI can be combined to solve real business problems at scale.

