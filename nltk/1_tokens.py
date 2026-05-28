import nltk
nltk.download('punkt_tab');

from nltk import word_tokenize,sent_tokenize

text = "the quick brown fox jumps over the lazy dog. dog had black color. dog was barking towards stranger person."

print(text)

#sentence tokenize 
print(sent_tokenize(text))

#word tokenize 
print(word_tokenize(text))


