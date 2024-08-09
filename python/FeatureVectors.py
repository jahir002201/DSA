from sklearn.feature_extraction.text import CountVectorizer

# Sample text data
texts = ["hello world", "hello from the other side"]

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the text data into feature vectors
X = vectorizer.fit_transform(texts)

# Print the feature vectors (as an array)
print("Feature Vectors:\n", X.toarray())

# Print the feature names (i.e., the vocabulary)
print("Feature Names:", vectorizer.get_feature_names_out())
