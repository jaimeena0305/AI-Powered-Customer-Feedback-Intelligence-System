from openai import OpenAI

client = OpenAI(api_key="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")

def classify_complaint(text):
    prompt = f"""
    You are a customer experience analyst.

    Classify this complaint into ONE category:
    - Delivery
    - Refund
    - Product Quality
    - Customer Support
    - Other

    Complaint: {text}

    Return only the category name.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


def summarize_feedback(reviews):
    prompt = f"""
    You are a business analyst.

    Summarize the following customer feedback
    and highlight major issues and positives:

    {reviews}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
