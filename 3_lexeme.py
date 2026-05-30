import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying a startup.")

for item in doc:
    lexeme = item.lex
    leema = item.lemma_ 
    print(f"Text: {lexeme.text}, Basic Meaning: {leema} Is Alpha: {lexeme.is_alpha}, Is Stop: {lexeme.is_stop}, Is Punct: {lexeme.is_punct} ")

