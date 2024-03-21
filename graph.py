import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the analyzed data
df = pd.read_csv('analyzed_customer_reviews.csv')

# Plot 1: Sentiment Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Sentiment_Label', palette='viridis')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Plot 2: Average Sentiment Score
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Sentiment_Label', y='Sentiment', palette='viridis', estimator=lambda x: sum(x)/len(x))
plt.title('Average Sentiment Score')
plt.xlabel('Sentiment')
plt.ylabel('Average Score')
plt.show()

# Plot 3: Histogram of Sentiment Scores
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Sentiment', bins=20, kde=True, color='skyblue')
plt.title('Histogram of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()
