import pandas as pd
from textblob import TextBlob

# Load the CSV file
df = pd.read_csv('customer_reviews.csv')

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(str(text))
    # Polarity ranges from -1 (most negative) to 1 (most positive)
    # Subjectivity ranges from 0 (very objective) to 1 (very subjective)
    return analysis.sentiment.polarity

# Apply sentiment analysis to each review
df['Sentiment'] = df['Review'].apply(analyze_sentiment)

# Classify sentiment as positive, negative, or neutral based on polarity
def get_sentiment_label(score):
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment labels
df['Sentiment_Label'] = df['Sentiment'].apply(get_sentiment_label)

# Save the analyzed data to a new CSV file
df.to_csv('analyzed_customer_reviews.csv', index=False)

# Display the DataFrame with sentiment analysis results
print(df)
