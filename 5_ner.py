import nltk
from nltk.tokenize import word_tokenize

# Downloads
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

text = "Google was founded by Larry Page and Sergey Brin in September 1998 in a garage in Menlo Park, California, USA."

# Step 1: Tokenize
tokens = word_tokenize(text)

# Step 2: POS Tagging
tagged = nltk.pos_tag(tokens)

# Step 3: Named Entity Recognition
entities = nltk.ne_chunk(tagged)

print(entities)