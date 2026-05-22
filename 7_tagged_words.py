import nltk 

nltk.download('brown')

from nltk.corpus import brown as bn 
print(bn.categories())

government = bn.words(categories='government')

print(len(government))
print(government[:50])
print(bn.tagged_words()[:50])
