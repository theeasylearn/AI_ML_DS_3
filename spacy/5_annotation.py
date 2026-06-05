import spacy as sa 

sp = sa.load('en_core_web_sm')

text = """Natural Language Processing (NLP) is a branch of Artificial Intelligence that helps computers understand and process human language. Companies like Google and Microsoft use NLP in products such as Google Translate and Copilot. On 15 January 2025, OpenAI launched advanced NLP updates for chat applications. Many NLP startups are also growing in cities like Bhavnagar and Ahmedabad. Elon Musk is the CEO of Tesla"""

doc = sp(text)
print(f"{'Text:':<10} {'pos_:':<10} {'dep_':<10} {'ent_type_':<15} {'fine_pos_':<10}  {'is_stop':<10} {'is_punct':<10}")
for token in doc:
    print(f"{token.text:<10} {token.pos_:<10} {token.dep_:<10} {token.ent_type_:<15} {token.tag_:<10} {str(token.is_stop):<10} {str(token.is_punct):<10}")
    

