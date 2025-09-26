from simple_salesforce import Salesforce
from textblob import TextBlob


# Connect to Salesforce
sf = Salesforce(
    username='your username',
    password='your password',
    security_token='your security token',
    domain='login'  # or 'test' if sandbox
)


print(" Logged into Salesforce!")


# Sentiment Analysis Function
def analyze_sentiment(text):
    blob = TextBlob(text)
    score = round(blob.sentiment.polarity, 3)  # score between -1 and 1
    if score > 0.2:
        return "Positive", score
    elif score < -0.2:
        return "Negative", score
    else:
        return "Neutral", score


# Query Unprocessed Feedback Records
query = """
    SELECT Id, Feedback_Text__c
    FROM CustomerFeedback__c
    WHERE Sentiment__c = NULL
    LIMIT 50
"""


results = sf.query(query)
records = results['records']


print(f"Found {len(records)} records to process.")


# Process Each Record
for rec in records:
    feedback_id = rec['Id']
    feedback_text = rec.get('Feedback_Text__c', '')


    if not feedback_text:
        print(f"Skipping record {feedback_id} - no feedback text.")
        continue


    sentiment, score = analyze_sentiment(feedback_text)


    # Update record in Salesforce
    sf.CustomerFeedback__c.update(feedback_id, {
        'Sentiment__c': sentiment,
        'Sentiment_Score__c': score,
        'Processed__c' : True
    })


    print(f"Updated record {feedback_id} → {sentiment} ({score})")


print("🎉 All feedback records processed.")

