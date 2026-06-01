import spacy as sa 

# nlp = sa.load('en_core_web_sm')
# python -m spacy download en_core_web_lg
nlp = sa.load('en_core_web_lg')

text = """
1. Bowler runs in, defended back to him. Score: 0/0 (0.1)
2. Left outside off stump. Score: 0/0 (0.2)
3. Single to square leg. Score: 1/0 (0.3)
4. Cover drive for FOUR. Score: 5/0 (0.4)
5. Beaten outside off stump. Score: 5/0 (0.5)
6. Single to midwicket. Score: 6/0 (1.0)
7. Pull shot for TWO. Score: 8/0 (1.2)
8. Straight drive for FOUR. Score: 12/0 (1.3)
9. Caught behind. WICKET. Score: 42/1 (5.1)
10. Lofted over long-on for SIX. Score: 59/1 (6.3)
"""

#create doc object

document = nlp(text)

#fetch each and every entity in text

count = 0
for entity in document.ents:
    print(f"Text = {entity.text:<30} Label = {entity.label_} ")
    count = count + 1

print("No of entity found = ",count)