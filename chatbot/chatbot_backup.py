import spacy as sa 
from knowledge_base import knowledge

nlp = sa.load('en_core_web_sm')

def greetings(message):
    list = ['hello', 'hi', 'hey', 'howdy', 'greetings', 'good morning', 'good afternoon', 'good evening', 'good day', "what's up", 'whats up', 'how are you', "how's it going", 'how do you do', 'nice to meet you', 'welcome', 'pleased to meet you', 'how have you been', 'good to see you', 'long time no see', 'good to meet you', 'hiya', 'yo', 'sup']
    if message.strip().lower() in list:
        return True

def goodbye(message):
    list = ['goodbye', 'bye', 'bye bye', 'see you', 'see you later', 'see you soon', 'take care', 'have a good day', 'have a nice day', 'farewell', 'so long', 'catch you later', 'talk to you later', 'until next time', 'later', 'cheers', 'good night', 'all the best', 'take it easy', 'nice meeting you', 'it was nice meeting you', 'peace', 'peace out', 'ttyl']
    if message.strip().lower() in list:
        return True

def preprocess(doc):
    best_answer = None
    best_score = 0

    for token in doc:
        if token.is_stop or token.is_punct or token.is_digit or token.like_num:
            continue
            
        # Use LEMMA for better matching
        token_lemma = token.lemma_.lower()
        token_text = token.text.lower()
        
        for topics in knowledge:
            for key in knowledge[topics]:
                topic_dict = knowledge[topics][key]
                
                if isinstance(topic_dict, dict) and 'keywords' in topic_dict:
                    keywords = [k.lower() for k in topic_dict['keywords']]
                    
                    score = 0
                    # Check both lemma and original text
                    if token_lemma in keywords or token_text in keywords:
                        score += 5
                    
                    # Bonus for partial match
                    for kw in keywords:
                        if token_lemma in kw or token_text in kw or kw in token_lemma:
                            score += 3
                    
                    if score > best_score:
                        best_score = score
                        best_answer = topic_dict['answer']

    if best_answer:
        print(best_answer)
    else:
        print("Bot: Sorry, I didn't understand that. Can you please rephrase?")

# ===================== MAIN LOOP =====================
while True:
    question = input("You : ")
    doc = nlp(question)  
    message = doc.text.strip().lower()
    
    if greetings(message):
        print("Bot: Hello! How can I help you?")
    elif goodbye(message):
        print("Bot : good bye, take care")
        break
    else:
        preprocess(doc)