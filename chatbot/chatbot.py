import spacy as sa 
from knowledge_base import knowledge

import datetime
import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

try:
    import openai
except ImportError:
    openai = None
    print("Warning: 'openai' package not installed. Run: pip install openai  (required for Grok)")

nlp = sa.load('en_core_web_sm')

# ===================== EMAIL CONFIGURATION =====================
# These can be updated here, or you will be prompted at runtime if they look like placeholders.
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "karan.bhatt.bhavnagar@gmail.com"       # <-- CHANGE THIS (use a valid Gmail)
SENDER_PASSWORD = "egzt szmf aklt yjsx"   # <-- CHANGE THIS (Gmail App Password)

RECEIVER_EMAIL = "theeasylearn@gmail.com"

# ===================== GROK / xAI CONFIG (for dynamic course questions) =====================
# Uses Grok (by xAI) - good alternative when you hit ChatGPT quota limits.
# 1. pip install openai
# 2. Get your xAI API key here: https://console.x.ai/
#    (Free tier available with good limits)
#    Keys start with "xai-"
# You can also set it via environment variable: XAI_API_KEY
XAI_API_KEY = os.getenv("XAI_API_KEY", "")
XAI_MODEL = "grok-3-1212"   # Good balance. Alternatives: "grok-3", "grok-2"


def greetings(message):
    greet_list = ['hello', 'hi', 'hey', 'howdy', 'greetings', 'good morning', 'good afternoon', 'good evening', 'good day', "what's up", 'whats up', 'how are you', "how's it going", 'how do you do', 'nice to meet you', 'welcome', 'pleased to meet you', 'how have you been', 'good to see you', 'long time no see', 'good to meet you', 'hiya', 'yo', 'sup']
    return message.strip().lower() in greet_list

def goodbye(message):
    bye_list = ['goodbye', 'bye', 'bye bye', 'see you', 'see you later', 'see you soon', 'take care', 'have a good day', 'have a nice day', 'farewell', 'so long', 'catch you later', 'talk to you later', 'until next time', 'later', 'cheers', 'good night', 'all the best', 'take it easy', 'nice meeting you', 'it was nice meeting you', 'peace', 'peace out', 'ttyl']
    return message.strip().lower() in bye_list

def preprocess(doc):
    global batch_timing_interest, interested_courses
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
        return f"Our contact number is {contact_data['mobile']}."
    elif asked_for_address and not asked_for_mobile and not asked_for_email and not asked_for_website:
        return f"Our institute location is: {contact_data['address']}."
    elif asked_for_email and not asked_for_mobile and not asked_for_address and not asked_for_website:
        return f"You can email us at {contact_data['email']}."
    elif asked_for_website and not asked_for_mobile and not asked_for_address and not asked_for_email:
        return f"Our official website is {contact_data['website']}."

    # ─────────────────────────────────────────────────────────
    # NEW STEP: DYNAMIC COURSE QUESTIONS via Grok (xAI)
    # Handles: who can join, salary for freshers, non-IT, minimum qualification,
    # maths requirement, which course for coding, need computer, english etc.
    # ─────────────────────────────────────────────────────────
    dynamic_advice = get_dynamic_course_advice(doc.text)
    if dynamic_advice:
        course_name, _ = extract_course_name(user_question)
        if course_name:
            interested_courses.add(course_name)
        return dynamic_advice

    # ─────────────────────────────────────────────────────────
    # STEP 2: SPECIFIC COURSE INTENT LOOKUP (fees, duration, topics)
    # ─────────────────────────────────────────────────────────
    courses_dict = knowledge['topics']['courses'].get('list', {})
    
    for course_key, course_info in courses_dict.items():
        course_keywords = [kw.lower() for kw in course_info['keywords']]
        
        if any(token_text == course_key or token_text in course_keywords for token_text in input_tokens_text):
            name = course_info['name']
            duration = course_info['duration']
            fees = course_info['fees']
            detail = course_info['details']
            
            # Track interest
            interested_courses.add(name)
            
            asked_for_fees = any(word in user_question for word in fee_intents)
            asked_for_duration = any(word in user_question for word in duration_intents)
            asked_for_topics = any(word in user_question for word in topic_intents)
            
            if asked_for_fees and not asked_for_duration and not asked_for_topics:
                return f"The fee for the {name} course is {fees}."
            elif asked_for_duration and not asked_for_fees and not asked_for_topics:
                return f"The duration of the {name} course is {duration}."
            elif asked_for_topics and not asked_for_fees and not asked_for_duration:
                return f"Here are the topics covered in {name}: {detail}"
            elif (asked_for_fees and asked_for_duration) or (asked_for_fees and asked_for_topics) or (asked_for_duration and asked_for_topics):
                response = f"For {name}:"
                if asked_for_fees: response += f"\n* Fees: {fees}"
                if asked_for_duration: response += f"\n* Duration: {duration}"
                if asked_for_topics: response += f"\n* Topics: {detail}"
                return response
            else:
                return f"Yes, we provide {name}.\n* Duration: {duration}\n* Fees: {fees}\n* Topics: {detail}"

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
                if topic_key == 'batch_timings':
                    batch_timing_interest = topic_dict.get('answer')

    if best_score > 0 and best_answer:
        return best_answer
    else:
        return "__TRIGGER_APPOINTMENT__"

# ===================== HELPER FUNCTIONS =====================

def log_interaction(question, answer):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        f.write(f"You: {question}\n")
        f.write(f"Bot: {answer}\n\n")


def send_email(to_email, subject, body, attachment_path=None):
    sender = SENDER_EMAIL
    password = SENDER_PASSWORD

    # Simulate if not properly configured
    if (not sender or "your_" in sender or "@" not in sender or
            not password or "your_" in password or password == "your_app_password_here"):
        print("\n=== [EMAIL SIMULATED - Configure SENDER_EMAIL / SENDER_PASSWORD for real sending] ===")
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print("Body:")
        print(body)
        if attachment_path and os.path.exists(attachment_path):
            print(f"[Attachment: {attachment_path}]")
        print("=== END SIMULATION ===\n")
        return True

    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(attachment_path)}'
            )
            msg.attach(part)

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully to", to_email)
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


def send_appointment_email(name, email, mobile, date, time_str, original_question=None):
    subject = f"New Counsellor Appointment Request - {name}"
    body = f"""Dear Team,

A user has requested an appointment with a counsellor.

User Details:
- Name: {name}
- Email: {email}
- Mobile: {mobile}

Appointment Details:
- Preferred Date: {date}
- Preferred Time: {time_str}

Original Question (unanswered): {original_question or 'N/A'}

Please contact the user to confirm the meeting.

Thank you,
EasyLearn Chatbot
"""
    send_email(RECEIVER_EMAIL, subject, body)


def send_final_summary_email():
    end_time = datetime.datetime.now()
    duration = end_time - conversation_start
    courses_str = ", ".join(sorted(interested_courses)) if interested_courses else "Not specified during chat"
    timings_str = batch_timing_interest or "Not specified during chat"

    subject = f"Chatbot Conversation Log - {user_name} ({user_email})"
    body = f"""Chatbot Conversation Summary for EasyLearn Academy

Conversation Date/Time: {conversation_start.strftime('%Y-%m-%d %H:%M:%S')} to {end_time.strftime('%Y-%m-%d %H:%M:%S')}
Duration: {duration}

User Details:
- Name: {user_name}
- Email: {user_email}
- Mobile: {user_mobile}

Interested Courses: {courses_str}
Preferred Timings: {timings_str}

The full conversation log (questions & answers) is attached as a text file.

---
This email was auto-generated by the EasyLearn Chatbot.
"""

    send_email(RECEIVER_EMAIL, subject, body, attachment_path=log_path)


def handle_unknown_question(question):
    print("Bot: Sorry, I don't have information about that in my current knowledge base.")
    choice = input("Would you like to book an appointment with our counsellor? (yes/no): ").strip().lower()
    if choice in ['yes', 'y', 'yeah', 'sure']:
        appt_date = input("Enter preferred date (YYYY-MM-DD): ").strip()
        appt_time = input("Enter preferred time (e.g. 11:00 AM): ").strip()
        send_appointment_email(user_name, user_email, user_mobile, appt_date, appt_time, question)
        confirmation = f"Thank you. Appointment request for {appt_date} at {appt_time} has been sent to our team."
        print(f"Bot: {confirmation}")
        return confirmation
    else:
        msg = "Okay. Please feel free to ask another question or rephrase."
        print(f"Bot: {msg}")
        return msg


# ===================== GROK / xAI DYNAMIC COURSE ADVICE HELPERS =====================

def configure_grok_if_needed():
    """Prompt user for xAI / Grok API key at startup if not configured."""
    global XAI_API_KEY
    if openai is None:
        return
    if (not XAI_API_KEY or "your-key" in XAI_API_KEY.lower() or not XAI_API_KEY.startswith("xai-")):
        print("\n[Grok / xAI Setup] To answer detailed course questions (eligibility, salary, maths, non-IT etc.) using Grok:")
        ans = input("Configure xAI API key now? (y/n): ").strip().lower()
        if ans in ["y", "yes"]:
            XAI_API_KEY = input("Paste your xAI API key (starts with xai-): ").strip()
        else:
            print("  → Dynamic answers will use fallback messages.\n")


def extract_course_name(question_lower: str):
    """Find if user mentioned a specific course. Returns (display_name, key) or (None, None)."""
    courses_dict = knowledge['topics']['courses'].get('list', {})
    for ckey, cinfo in courses_dict.items():
        kws = [kw.lower() for kw in cinfo.get('keywords', [])] + [ckey.lower()]
        for kw in kws:
            if kw in question_lower:
                return cinfo['name'], ckey
    # Also try common spoken variants
    spoken_map = {
        'full stack': 'mern', 'fullstack': 'mern', 'mern stack': 'mern',
        'ai': 'ai_ml', 'machine learning': 'ai_ml', 'artificial intelligence': 'ai_ml',
        'data science': 'data_science', 'datascience': 'data_science',
        'web design': 'web_design', 'web designing': 'web_design',
        'android': 'android', 'mobile app': 'android',
        'cyber': 'cyber_security', 'ethical hacking': 'cyber_security',
        'ui ux': 'ui_ux', 'uiux': 'ui_ux', 'ux': 'ui_ux'
    }
    for phrase, ckey in spoken_map.items():
        if phrase in question_lower:
            return courses_dict.get(ckey, {}).get('name'), ckey
    return None, None


def ask_grok(system_prompt: str, user_prompt: str) -> str:
    """Call Grok via xAI API (OpenAI-compatible endpoint)."""
    if openai is None or not XAI_API_KEY or not XAI_API_KEY.startswith("xai-"):
        return None  # caller will handle fallback

    try:
        client = openai.OpenAI(
            api_key=XAI_API_KEY,
            base_url="https://api.x.ai/v1"
        )
        resp = client.chat.completions.create(
            model=XAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.65,
            max_tokens=280
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, I couldn't fetch the latest information from the internet right now. ({str(e)[:80]})"


def get_dynamic_course_advice(user_question: str) -> str | None:
    """
    Detects the special course-related questions listed by user.
    If matched, fetches fresh answer via Grok (xAI).
    """
    q = user_question.lower().strip()

    # Keywords that signal the listed question types (1-8)
    advice_triggers = [
        'who can join', 'eligibility', 'eligible', 'can i join', 'suitable for whom',
        'salary', 'ctc', 'package', 'fresher', 'freshers', 'expected salary', 'what salary',
        'non it', 'non-it', 'nonit', 'non it candidate', 'commerce', 'arts', 'other field',
        'minimum qualification', 'bare minimum', 'what qualification', '10th', '12th pass',
        'maths', 'math', 'mathematics', 'need maths', 'expert in math',
        'learn coding', 'which course should i', 'which course to select', 'best course for coding',
        'need a computer', 'need laptop', 'have computer', 'do i need pc',
        'know english', 'english required', 'good in english', 'language required'
    ]

    if not any(trigger in q for trigger in advice_triggers):
        return None

    course_name, course_key = extract_course_name(q)

    # Build context-aware prompt
    if course_name:
        context = f"the {course_name} course"
    else:
        context = "IT courses (Python, Full Stack, Data Science, AI/ML, etc.)"

    system = (
        "You are an honest and encouraging career counsellor for EasyLearn Academy, "
        "an IT training institute in Bhavnagar, Gujarat. "
        "Answer questions about course eligibility, fresher salaries in India, prerequisites, "
        "suitability for non-IT / commerce / arts students, and whether maths or English is required. "
        "Be practical, realistic, and a bit direct (Grok style). Use current Indian job market context (2025-2026). "
        "Keep replies short, friendly, and in plain English (4-8 sentences max)."
    )

    user_prompt = f"""User question about {context}:
"{user_question}"

Please give a direct and helpful answer. 
If talking about salary, mention realistic fresher CTC range in Indian companies (product vs service, tier-1/2/3 cities).
If about eligibility or background, clearly say whether non-IT students can join and what minimum qualification is needed.
If about coding which course to pick, give 1-2 best recommendations with reason.
"""

    ai_answer = ask_grok(system, user_prompt)
    if ai_answer:
        return ai_answer

    # Fallback message when API not available
    return (
        "For the most accurate and latest information on eligibility, salaries, and requirements, "
        "I recommend checking with our counsellors or visiting https://theeasylearnacademy.com/. "
        "In general, most of our courses welcome students from any background (10th/12th pass and above)."
    )


# ===================== MAIN LOOP =====================

# --- Task 1: Collect user details at start ---
print("Welcome to EasyLearn Academy Chatbot!")
print("To assist you better, please provide your details.")
user_name = input("Enter your name: ").strip()
user_email = input("Enter your email: ").strip()
user_mobile = input("Enter your mobile number: ").strip()

# Optional: configure sender for email if placeholders are still in place (for Tasks 3 & 4)
if (not SENDER_EMAIL or "your_" in SENDER_EMAIL or "@" not in SENDER_EMAIL or
        not SENDER_PASSWORD or "your_" in SENDER_PASSWORD):
    print("\n[Email Setup] To enable sending appointment requests and final chat log (recommended):")
    print("  Use a Gmail address + App Password (create at myaccount.google.com/apppasswords).")
    setup = input("Do you want to enter Gmail credentials now for sending emails? (y/n): ").strip().lower()
    if setup in ['y', 'yes']:
        SENDER_EMAIL = input("  Sender Gmail: ").strip()
        SENDER_PASSWORD = input("  App Password (input hidden in real but shown here for demo): ").strip()
    else:
        print("  (Emails will be simulated. Edit the script or re-run to provide credentials.)\n")

# Configure Grok (xAI) for dynamic answers (new feature)
configure_grok_if_needed()

conversation_start = datetime.datetime.now()

# Setup log file (Task 2)
os.makedirs("chat_logs", exist_ok=True)
safe_name = user_name.replace(" ", "_") if user_name else "anonymous"
log_filename = f"chat_log_{safe_name}_{conversation_start.strftime('%Y%m%d_%H%M%S')}.txt"
log_path = os.path.join("chat_logs", log_filename)

# Initialize tracking for interests (used for Task 4)
interested_courses = set()
batch_timing_interest = None

# Write header to log file
with open(log_path, "w", encoding="utf-8") as f:
    f.write("EASYLEARN ACADEMY - CHATBOT CONVERSATION LOG\n")
    f.write(f"Start Time: {conversation_start.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Name: {user_name}\n")
    f.write(f"Email: {user_email}\n")
    f.write(f"Mobile: {user_mobile}\n")
    f.write("=" * 60 + "\n\n")

print(f"\nBot: Thank you, {user_name}! How can I help you today?\n")
print("Bot: (Ask about course fees, duration, or questions like 'who can join python?', 'salary after data science', 'non IT for AI ML', etc. Powered by Grok)\n")

while True:
    question = input("You : ")
    doc = nlp(question)  
    message = doc.text.strip().lower()
    
    if greetings(message):
        reply = "Hello! How can I help you?"
        print(f"Bot: {reply}")
        log_interaction(question, reply)
    elif goodbye(message):
        reply = "Goodbye, take care!"
        print(f"Bot: {reply}")
        log_interaction(question, reply)
        
        # Task 4: Send log file + summary via email when chat finishes
        print("\nBot: Thank you for chatting with us. Sending your conversation details to our team...")
        
        # Append final summary line to the log file
        end_time = datetime.datetime.now()
        courses_str = ", ".join(sorted(interested_courses)) if interested_courses else "Not specified"
        timings_str = batch_timing_interest or "Not specified"
        with open(log_path, "a", encoding="utf-8") as f:
            f.write("\n" + "=" * 60 + "\n")
            f.write(f"CONVERSATION ENDED: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Interested Courses: {courses_str}\n")
            f.write(f"Preferred Timings: {timings_str}\n")
        
        send_final_summary_email()
        print("Bot: Details have been emailed. Have a great day!")
        break
    else:
        bot_reply = preprocess(doc)
        if bot_reply == "__TRIGGER_APPOINTMENT__":
            # Task 3: Unknown question -> offer counsellor appointment
            bot_reply = handle_unknown_question(question)
            log_interaction(question, bot_reply)
        else:
            print(f"Bot: {bot_reply}")
            log_interaction(question, bot_reply)