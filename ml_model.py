import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
df = pd.read_csv("data.csv")

# Labels (1 = Positive, 0 = Negative)
labels = [0,1,0,1,0,1,0,0,1,0]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["review"])

# Train ML model
model = LogisticRegression()
model.fit(X, labels)

# Save model files
pickle.dump(model, open("sentiment_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Sentiment model trained successfully!")
