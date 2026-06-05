import spacy as sa 

# nlp = sa.load('en_core_web_sm')
# python -m spacy download en_core_web_lg
nlp = sa.load('en_core_web_lg')

text = "On 15 January 2025, Ankit Patel from Bhavnagar, Gujarat, India joined OpenAI as a Software Engineer and attended the AI Innovation Summit 2025 at Taj Palace Hotel, New Delhi, where he discussed Python, GPT-5, and a project worth ₹5,00,000 before flying on Air India Flight AI101 to Mumbai"

#create doc object

document = nlp(text)

#fetch each and every entity in text

count = 0
for entity in document.ents:
    print(f"Text = {entity.text:<30} Label = {entity.label_} ")
    count = count + 1

print("No of entity found = ",count)