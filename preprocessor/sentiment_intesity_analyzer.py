from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Example batch of sentences
sentences = ["I love this movie", "I hate this food", "The weather is nice today"]

# Get the sentiment scores for each sentence in the batch
scores = [sia.polarity_scores(sentence)['compound'] for sentence in sentences]

# Convert the continuous scores to binary labels
threshold = 0.0
labels = np.array(scores) > threshold

print(labels)
