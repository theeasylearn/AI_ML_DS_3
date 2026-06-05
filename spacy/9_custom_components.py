import spacy as sa 
from spacy.language import Language
from spacy.tokens import Doc

courses = [
    "Artificial Intelligence (AI) & Machine Learning",
    "Data Science & Data Analytics",
    "Generative AI & Large Language Models (LLMs)",
    "Cloud Computing (AWS, Azure, Google Cloud)",
    "Cybersecurity & Ethical Hacking",
    "Full Stack Web Development",
    "DevOps & Site Reliability Engineering (SRE)",
    "Python Programming",
    "Blockchain Technology & Web3",
    "UI/UX Design with Figma and Design Systems"
]
#property 
Doc.set_extension("courses",default=[])
text = """Artificial Intelligence (AI) & Machine Learning is transforming industries by enabling computers to learn from data, make predictions, and automate complex tasks. Many organizations are investing heavily in AI solutions to improve efficiency and customer experiences. Data Science & Data Analytics plays a crucial role in extracting valuable insights from large datasets, helping businesses make informed decisions and identify new opportunities. Professionals with strong analytical skills are highly sought after across various sectors. Generative AI & Large Language Models (LLMs) represent the next evolution of artificial intelligence, allowing systems to create content, answer questions, generate code, and assist users in innovative and productive ways.
"""
@Language.component("getCourses")
def getCourses(doc):
    doc_text = doc.text
    list = []
    for course in courses:
        if course in doc_text:
            list.append(course)
    doc._.courses = list
    return doc

nlp = sa.load('en_core_web_sm')
nlp.add_pipe("getCourses",last=True)
doc = nlp(text)
print(doc._.courses)

