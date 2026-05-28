import spacy as sa 
#load english model
nlp = sa.load('en_core_web_sm')
paragraph = """Natural Language Processing (NLP) is a branch of Artificial Intelligence that helps computers understand and process human language. Companies like Google and Microsoft use NLP in products such as Google Translate and Copilot. On 15 January 2025, OpenAI launched advanced NLP updates for chat applications. Many NLP startups are also growing in cities like Bhavnagar and Ahmedabad. Elon Musk is the CEO of Tesla
"""
#create doc object
doc = nlp(paragraph)
print("Generating span of 3 token...")
span_1 = doc[0:3]
print(span_1)

print("Generating span of last token...")
span_2 = doc[-4:]
print(span_2)
