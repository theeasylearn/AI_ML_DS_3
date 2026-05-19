from nltk import WordNetLemmatizer

wm = WordNetLemmatizer()

words = [
    "better",       # Irregular adjective (should lemmatize to "good" with proper POS tag)
    "was",          # Irregular verb (should lemmatize to "be")
    "mice",         # Irregular plural noun (should lemmatize to "mouse")
    "flying",       # Verb gerund/participle (should lemmatize to "fly")
    "leaves",       # Ambiguous plural/verb (should lemmatize to "leaf" or "leave")
    "studies",      # Third-person singular verb (should lemmatize to "study")
    "hardest",      # Superlative adjective (should lemmatize to "hard")
    "corpora",      # Foreign/Latin plural noun (should lemmatize to "corpus")
    "fulfilled",    # Past tense verb with consonant doubling (should lemmatize to "fulfill")
    "oxen"          # Irregular plural noun (should lemmatize to "ox")
]

for item in words:
    print(wm.lemmatize(item))
