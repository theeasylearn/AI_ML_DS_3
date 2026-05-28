import nltk
from nltk.tokenize import word_tokenize

text = """The Spirit of India
India is a land of diversity, culture, and history. From the snowy Himalayas in the north to the beautiful beaches in the south, every part of India has its own beauty. People speak different languages, celebrate many festivals, and follow various traditions, yet they live together with unity and respect. India is famous for yoga, delicious food, classical music, and ancient monuments like the Taj Mahal. Farmers, scientists, teachers, and soldiers all contribute to the nation’s growth. The country is also growing rapidly in technology and education. India teaches the world the values of peace, family, and harmony among different communities."""

token = word_tokenize(text)
print(token)

tags = nltk.pos_tag(token)
print(tags)