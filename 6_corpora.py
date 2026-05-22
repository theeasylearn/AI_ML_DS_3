import nltk 

nltk.download('gutenberg')

from nltk.corpus import gutenberg as gt 
print(gt.fileids())


book = gt.words('shakespeare-hamlet.txt')
#here book is one type of list 

total_words = len(book)
print(total_words)

#display 50 words
print(book[:50])