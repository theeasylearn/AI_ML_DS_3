from nltk import PorterStemmer

ps = PorterStemmer()

words = ["running", "flies", "happily", "maximum", "biological", "grew", "connections", "feet", "adjustable", "denied"]

list = []
for item in words:
    list.append(ps.stem(item))
print(list)