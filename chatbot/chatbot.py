import spacy as sa 
from knowledge_base import knowledge

nlp = sa.load('en_core_web_sm')

def greetings(message):
    greet_list = ['hello', 'hi', 'hey', 'howdy', 'greetings', 'good morning', 'good afternoon', 'good evening', 'good day', "what's up", 'whats up', 'how are you', "how's it going", 'how do you do', 'nice to meet you', 'welcome', 'pleased to meet you', 'how have you been', 'good to see you', 'long time no see', 'good to meet you', 'hiya', 'yo', 'sup']
    return message.strip().lower() in greet_list

def goodbye(message):
    bye_list = ['goodbye', 'bye', 'bye bye', 'see you', 'see you later', 'see you soon', 'take care', 'have a good day', 'have a nice day', 'farewell', 'so long', 'catch you later', 'talk to you later', 'until next time', 'later', 'cheers', 'good night', 'all the best', 'take it easy', 'nice meeting you', 'it was nice meeting you', 'peace', 'peace out', 'ttyl']
    return message.strip().lower() in bye_list

def preprocess(doc):
    best_answer = None
    best_score = 0
    
    # Normalize the entire input string to check for clear contextual intents
    user_question = doc.text.lower()
    input_tokens_text = [token.text.lower() for token in doc if not token.is_punct]

    # Intent Keyword Buckets
    fee_intents = ['fee', 'fees', 'cost', 'price', 'charges', 'pricing', 'how much', 'rs', 'rupees', 'amount', 'pay']
    duration_intents = ['duration', 'long', 'month', 'months', 'week', 'weeks', 'days', 'time', 'period']
    topic_intents = ['topic', 'topics', 'syllabus', 'detail', 'details', 'learn', 'teach', 'cover', 'covers', 'content']
    
    # Granular Contact Intent Buckets
    mobile_intents = ['mobile', 'number', 'phone', 'contact no', 'contact number', 'call', 'whatsapp']
    address_intents = ['address', 'location', 'where', 'situated', 'place', 'office', 'landmark', 'map', 'directions']
    email_intents = ['email', 'mail', 'gmail']
    website_intents = ['website', 'site', 'url', 'link', 'online link']

    # ─────────────────────────────────────────────────────────
    # STEP 1: GRANULAR CONTACT AND LOCATION INTENT PROCESSING
    # ─────────────────────────────────────────────────────────
    contact_data = knowledge['topics']['contact'].get('details', {})
    
    asked_for_mobile = any(word in user_question for word in mobile_intents)
    asked_for_address = any(word in user_question for word in address_intents)
    asked_for_email = any(word in user_question for word in email_intents)
    asked_for_website = any(word in user_question for word in website_intents)
    
    # Check if user explicitly asked for individual specific contact fields
    if asked_for_mobile and not asked_for_address and not asked_for_email and not asked_for_website:
        print(f"Bot: Our contact number is {contact_data['mobile']}.")
        return
    elif asked_for_address and not asked_for_mobile and not asked_for_email and not asked_for_website:
        print(f"Bot: Our institute location is: {contact_data['address']}.")
        return
    elif asked_for_email and not asked_for_mobile and not asked_for_address and not asked_for_website:
        print(f"Bot: You can email us at {contact_data['email']}.")
        return
    elif asked_for_website and not asked_for_mobile and not asked_for_address and not asked_for_email:
        print(f"Bot: Our official website is {contact_data['website']}.")
        return

    # ─────────────────────────────────────────────────────────
    # STEP 2: SPECIFIC COURSE INTENT LOOKUP
    # ─────────────────────────────────────────────────────────
    courses_dict = knowledge['topics']['courses'].get('list', {})
    
    for course_key, course_info in courses_dict.items():
        course_keywords = [kw.lower() for kw in course_info['keywords']]
        
        if any(token_text == course_key or token_text in course_keywords for token_text in input_tokens_text):
            name = course_info['name']
            duration = course_info['duration']
            fees = course_info['fees']
            detail = course_info['details']
            
            asked_for_fees = any(word in user_question for word in fee_intents)
            asked_for_duration = any(word in user_question for word in duration_intents)
            asked_for_topics = any(word in user_question for word in topic_intents)
            
            if asked_for_fees and not asked_for_duration and not asked_for_topics:
                print(f"Bot: The fee for the {name} course is {fees}.")
                return
            elif asked_for_duration and not asked_for_fees and not asked_for_topics:
                print(f"Bot: The duration of the {name} course is {duration}.")
                return
            elif asked_for_topics and not asked_for_fees and not asked_for_duration:
                print(f"Bot: Here are the topics covered in {name}: {detail}")
                return
            elif (asked_for_fees and asked_for_duration) or (asked_for_fees and asked_for_topics) or (asked_for_duration and asked_for_topics):
                response = f"Bot: For {name}:"
                if asked_for_fees: response += f"\n* Fees: {fees}"
                if asked_for_duration: response += f"\n* Duration: {duration}"
                if asked_for_topics: response += f"\n* Topics: {detail}"
                print(response)
                return
            else:
                print(f"Bot: Yes, we provide {name}.\n* Duration: {duration}\n* Fees: {fees}\n* Topics: {detail}")
                return

    # ─────────────────────────────────────────────────────────
    # STEP 3: FALLBACK TO GENERAL TOPICS KEYWORDS
    # ─────────────────────────────────────────────────────────
    for topic_key, topic_dict in knowledge['topics'].items():
        if 'keywords' in topic_dict:
            keywords = [k.lower() for k in topic_dict['keywords']]
            score = 0
            
            for token in doc:
                if token.is_stop or token.is_punct or token.is_digit or token.like_num:
                    continue
                
                t_lemma = token.lemma_.lower()
                t_text = token.text.lower()
                
                if t_lemma in keywords or t_text in keywords:
                    score += 5
                
                for kw in keywords:
                    if t_lemma in kw or t_text in kw or kw in t_lemma:
                        score += 3
            
            if score > best_score:
                best_score = score
                best_answer = topic_dict['answer']

    if best_score > 0 and best_answer:
        print(f"Bot: {best_answer}")
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
        print("Bot: Goodbye, take care!")
        break
    else:
        preprocess(doc)