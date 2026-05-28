import spacy as sa 

#load english model
nlp = sa.load('en_core_web_sm')


paragraph = """Natural Language Processing (NLP) is a branch of Artificial Intelligence that helps computers understand and process human language. Companies like Google and Microsoft use NLP in products such as Google Translate and Copilot. On 15 January 2025, OpenAI launched advanced NLP updates for chat applications. Many NLP startups are also growing in cities like Bhavnagar and Ahmedabad. Elon Musk is the CEO of Tesla

"""
#create doc object
doc = nlp(paragraph)
print("Generating tokens...")
for token in doc:
    print(token)

print("-"*100)
print("Generating Named Entity ...")
for entity in doc.ents:
    print(f"{entity.text} {entity.label_}")

