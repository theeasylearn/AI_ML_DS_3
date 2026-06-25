import spacy as sa 
nlp = sa.load('en_core_web_sm')
def greetings(message):
    list = ['hello', 'hi', 'hey', 'howdy', 'greetings', 'good morning', 'good afternoon', 'good evening', 'good day', "what's up", 'whats up', 'how are you', "how's it going", 'how do you do', 'nice to meet you', 'welcome', 'pleased to meet you', 'how have you been', 'good to see you', 'long time no see', 'good to meet you', 'hiya', 'yo', 'sup']
    if message in list:
        return True
def goodbye(message):
    list = ['goodbye', 'bye', 'bye bye', 'see you', 'see you later', 'see you soon', 'take care', 'have a good day', 'have a nice day', 'farewell', 'so long', 'catch you later', 'talk to you later', 'until next time', 'later', 'cheers', 'good night', 'all the best', 'take it easy', 'nice meeting you', 'it was nice meeting you', 'peace', 'peace out', 'ttyl']
    if message in list:
        return True
def preprocess(message):
    doc = nlp(message)
    message = doc.text.strip().lower()
    
while True:
    question = input("You : ")
    preprocess(question)