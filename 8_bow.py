from sklearn.feature_extraction.text import CountVectorizer

# Sample sentences
documents = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "The cat chased the mouse",
    "The dog chased the cat"
]

#create object of CountVectorizer
cv = CountVectorizer()
bow = cv.fit_transform(documents)

print("Vocabulary count ",cv.vocabulary_)
feature_names = cv.get_feature_names_out()
print(feature_names)
print(bow.toarray())