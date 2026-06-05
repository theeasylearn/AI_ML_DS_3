import spacy as sa 
nlp = sa.load('en_core_web_sm')

print("Pipeline content")
for name,component in nlp.pipeline:
    print(f"{name} {component}")
