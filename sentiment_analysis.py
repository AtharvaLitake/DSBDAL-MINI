import pandas as pd
from textblob import TextBlob

# Define the path to your CSV file
data_path = "./DSBDAL_mini.csv"

# Read the CSV data into a pandas DataFrame
data = pd.read_csv(data_path)

# Function to perform sentiment analysis on a single review
def analyze_sentiment(review):
  # Create a TextBlob object from the review text
  blob = TextBlob(review)

  # Get sentiment polarity (positive: 1, negative: -1, neutral: 0)
  sentiment = blob.sentiment.polarity

  return sentiment

# Add a new column for sentiment score to the DataFrame
data["sentiment_score"] = data["review"].apply(analyze_sentiment)

# Calculate overall sentiment statistics
average_sentiment = data["sentiment_score"].mean()
positive_reviews = len(data[data["sentiment_score"] > 0])
negative_reviews = len(data[data["sentiment_score"] < 0])

# Print results
print("Average Sentiment Score:", average_sentiment)
print("Positive Reviews:", positive_reviews)
print("Negative Reviews:", negative_reviews)

# Loop through each review for individual sentiment analysis (optional)
for index, row in data.iterrows():
  username = row["username"]
  review = row["review"]
  sentiment = row["sentiment_score"]

  print(f"Username: {username}, Review: {review}, Sentiment: {sentiment}")
