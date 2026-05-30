import spacy as sa 

sp = sa.load('en_core_web_sm')

text = """Natural Language Processing (NLP) is a branch of Artificial Intelligence that helps computers understand and process human language. Companies like Google and Microsoft use NLP in products such as Google Translate and Copilot. On 15 January 2025, OpenAI launched advanced NLP updates for chat applications. Many NLP startups are also growing in cities like Bhavnagar and Ahmedabad. Elon Musk is the CEO of Tesla"""

doc = sp(text)
for sentence in doc.sents:
    print(sentence.text)

