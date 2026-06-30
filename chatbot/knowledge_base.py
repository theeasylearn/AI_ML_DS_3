knowledge = {
    'topics': {
        # ─────────────────────────────────────────────
        # 1. ABOUT THE ACADEMY
        # ─────────────────────────────────────────────
        'about': {
            'keywords': ['about', 'tell me about', 'easylearn', 'academy', 'who are you', 'introduction', 'organization', 'what do you do', 'overview', 'info', 'information', 'background', 'history', 'founded', 'establishment'],
            'answer': """EasyLearn Academy is an IT training institute in Bhavnagar, Gujarat. We focus on practical courses with live projects, especially in web and mobile app development. We also provide corporate training and offshore development services. Our main goal is to make students job-ready with real skills."""
        },

        # ─────────────────────────────────────────────
        # 2. LOCATION / ADDRESS
        # ─────────────────────────────────────────────
        'location': {
            'keywords': ['location', 'address', 'where', 'place', 'situated', 'find you', 'directions', 'how to reach', 'map', 'navigate', 'office', 'city', 'state', 'gujarat', 'bhavnagar', 'visit', 'near', 'landmark', 'pincode', 'area', 'road', 'mall', 'institute location', 'academy location', 'institute address', 'academy address', 'where is institute', 'where is academy','institute','class'],
            'answer': """We are located at Eva Surbhi Mall, 105, Waghawadi Road, opposite Aksharwadi Temple, Bhavnagar, Gujarat - 364002. You can visit us Monday to Saturday. Check our website for more details: https://theeasylearnacademy.com/"""
        },

        # ─────────────────────────────────────────────
        # 3. COURSES (Restructured for Granular Access)
        # ─────────────────────────────────────────────
        'courses': {
            'keywords': ['courses', 'course', 'what do you teach', 'program', 'programs', 'subjects', 'curriculum', 'training', 'learn', 'study', 'available', 'offer', 'list of courses', 'which course', 'what courses'],
            'answer': """We offer courses in Python, Java, Full Stack MERN, PHP, Web Design, Android Development, AI/ML, Data Science, Cyber Security, UI/UX, CCC, and Tally. Contact us for fees and duration of any course.""",
            
            'list': {
                'python': {
                    'name': 'Python Programming',
                    'keywords': ['python', 'py'],
                    'duration': '3 months',
                    'fees': '₹15,000',
                    'details': 'Covers core Python, advanced concepts, and database integration with live projects.'
                },
                'java': {
                    'name': 'Java Development',
                    'keywords': ['java', 'core java', 'advanced java'],
                    'duration': '4 months',
                    'fees': '₹18,000',
                    'details': 'Focuses on Object-Oriented Programming, Core Java, JDBC, Servlets, and corporate backend architecture.'
                },
                'mern': {
                    'name': 'Full Stack MERN',
                    'keywords': ['mern', 'full stack', 'react', 'node', 'mongodb', 'express', 'fullstack web'],
                    'duration': '6 months',
                    'fees': '₹35,000',
                    'details': 'Complete end-to-end web development mastering MongoDB, Express.js, React, and Node.js.'
                },
                'php': {
                    'name': 'PHP Web Development',
                    'keywords': ['php', 'web development', 'mysql'],
                    'duration': '3 months',
                    'fees': '₹12,000',
                    'details': 'Backend development focusing on PHP scripting, MySQL database design, and framework architectures.'
                },
                'web_design': {
                    'name': 'Web Design',
                    'keywords': ['web design', 'html', 'css', 'javascript', 'bootstrap', 'front end', 'frontend design'],
                    'duration': '3 months',
                    'fees': '₹12,000',
                    'details': 'Covers HTML5, CSS3, JavaScript, Bootstrap, and responsive UI layout styling.'
                },
                'android': {
                    'name': 'Android Development',
                    'keywords': ['android', 'mobile app', 'app development', 'kotlin', 'java android'],
                    'duration': '4 months',
                    'fees': '₹20,000',
                    'details': 'Native mobile app development designing user interfaces, handling APIs, and local app data storing.'
                },
                'ai_ml': {
                    'name': 'Artificial Intelligence & Machine Learning',
                    'keywords': ['ai', 'ml', 'artificial intelligence', 'machine learning'],
                    'duration': '6 months',
                    'fees': '₹41,000',
                    'details': 'Focuses on predictive modeling, supervised/unsupervised machine learning algorithms, and neural networks.'
                },
                'data_science': {
                    'name': 'Data Science',
                    'keywords': ['data science', 'pandas', 'numpy', 'data analytics', 'analytics'],
                    'duration': '6 months',
                    'fees': '₹40,000',
                    'details': 'Covers data preprocessing, statistical operations, Pandas, NumPy, data visualization, and insights generation.'
                },
                'cyber_security': {
                    'name': 'Cyber Security',
                    'keywords': ['cyber security', 'ethical hacking', 'network security', 'security'],
                    'duration': '4 months',
                    'fees': '₹25,000',
                    'details': 'Focuses on structural network configurations, system vulnerabilities assessment, and threat mitigation mechanisms.'
                },
                'ui_ux': {
                    'name': 'UI/UX Design',
                    'keywords': ['ui', 'ux', 'ui/ux', 'figma', 'photoshop', 'wireframing', 'prototyping'],
                    'duration': '3 months',
                    'fees': '₹15,000',
                    'details': 'User journey planning, user experience research, wireframing, and professional high-fidelity prototyping using Figma.'
                },
                'ccc': {
                    'name': 'CCC (Course on Computer Concepts)',
                    'keywords': ['ccc', 'computer concepts', 'basic computer', 'office automation'],
                    'duration': '2 months',
                    'fees': '₹4,000',
                    'details': 'Fundamental digital literacy including hardware components, operating systems, internet usage, and office suites.'
                },
                'tally': {
                    'name': 'Tally Prime with GST',
                    'keywords': ['tally', 'accounting', 'gst', 'finance', 'bookkeeping'],
                    'duration': '2 months',
                    'fees': '₹6,000',
                    'details': 'Professional accounting software operations, balancing ledgers, inventory management, and structural GST calculations.'
                }
            }
        },

        # ─────────────────────────────────────────────
        # 4. TRAINING METHODOLOGY
        # ─────────────────────────────────────────────
        'training_methodology': {
            'keywords': ['training', 'methodology', 'teaching', 'how do you teach', 'practical', 'theoretical', 'hands on', 'hands-on', 'learn', 'style', 'approach', 'method', 'real world', 'projects', 'live project', 'experience', 'session', 'class', 'lecture', 'workshop', 'learning style', 'mode of training', 'interactive', 'industry ready', 'modern', 'technique'],
            'answer': """We focus on 100% practical training with live industry projects. Classes are conducted in small batches so every student gets personal attention. Our trainers are experienced and we use the latest tools and technologies."""
        },

        # ─────────────────────────────────────────────
        # 5. PLACEMENT
        # ─────────────────────────────────────────────
        'placement': {
            'keywords': ['placement', 'job', 'career', 'hire', 'hiring', 'employment', 'internship', 'opportunity', 'recruitment', 'company', 'companies', 'placed', 'get job', 'job support', 'job assistance', 'after course', 'work', 'industry', 'it company', 'salary', 'package', 'fresher', 'campus', 'interview', 'preparation', 'resume', 'cv', 'job ready', '100% placement'],
            'answer': """We provide full placement assistance including resume building, mock interviews, and direct referrals to companies. Many of our students have been placed in good IT companies."""
        },

        # ─────────────────────────────────────────────
        # 6. CORPORATE TRAINING & OFFSHORE
        # ─────────────────────────────────────────────
        'corporate_training': {
            'keywords': ['corporate', 'corporate training', 'offshore', 'multinational', 'company training', 'employee training', 'business', 'enterprise', 'organization training', 'b2b', 'team training', 'staff training', 'software development', 'outsourcing', 'project outsource', 'it services', 'development services', 'hire for project', 'custom training', 'group training', 'professional training'],
            'answer': """We offer custom corporate training for company teams as well as offshore development services for web and mobile applications. Feel free to contact us for your requirements."""
        },

        # ─────────────────────────────────────────────
        # 7. CONTACT DETAILS (Restructured for Granular Access)
        # ─────────────────────────────────────────────
        'contact': {
            'keywords': ['contact', 'reach', 'call', 'phone', 'number', 'mobile', 'cellphone', 'email', 'mail', 'whatsapp', 'message', 'enquiry', 'inquiry', 'get in touch', 'support', 'help', 'connect', 'talk', 'speak', 'chat', 'customer care', 'helpline', 'toll free', 'reach out', 'how to contact', 'contact details', 'social media', 'facebook', 'instagram', 'linkedin', 'website', 'url', 'link', 'online link', 'site'],
            'answer': """You can reach us at Eva Surbhi Mall, 105, Waghawadi Road, Bhavnagar. Visit our website https://theeasylearnacademy.com/ for phone, email, and WhatsApp details. We are available Monday to Saturday, 9 AM to 7 PM.""",
            
            # Granular data attributes for clean targeted responses
            'details': {
                'mobile': '+91 98765 43210',  # Replace with actual contact number
                'address': 'Eva Surbhi Mall, 105, Waghawadi Road, opposite Aksharwadi Temple, Bhavnagar, Gujarat - 364002.',
                'email': 'info@theeasylearnacademy.com',  # Replace with actual corporate email
                'website': 'https://theeasylearnacademy.com/'
            }
        },

        # ─────────────────────────────────────────────
        # 8. GENERAL FEES & DURATION INFO
        # ─────────────────────────────────────────────
        'fees_and_duration': {
            'keywords': ['fees', 'fee', 'cost', 'price', 'charges', 'pricing', 'how much', 'rate', 'amount', 'payment', 'pay', 'installment', 'emi', 'discount', 'scholarship', 'offer', 'affordable', 'duration', 'how long', 'months', 'weeks', 'days', 'hours', 'length', 'time', 'period', 'complete', 'finish', 'course duration', 'course fee', 'total cost'],
            'answer': """Course duration ranges from 1 to 6 months depending on the course. Our fees are very affordable with EMI options available. Please contact us for exact fees and current offers."""
        },

        # ─────────────────────────────────────────────
        # 9. BATCH TIMINGS
        # ─────────────────────────────────────────────
        'batch_timings': {
            'keywords': ['batch', 'timing', 'schedule', 'time', 'slot', 'session', 'morning', 'evening', 'weekend', 'weekday', 'saturday', 'sunday', 'monday', 'class time', 'when', 'next batch', 'start date', 'joining', 'new batch', 'online', 'offline', 'flexible', 'timetable', 'availability', 'shift'],
            'answer': """We have morning, afternoon, and evening batches. Weekend batches are also available. New batches start every month. Both online and offline modes are offered."""
        },

        # ─────────────────────────────────────────────
        # 10. CERTIFICATES
        # ─────────────────────────────────────────────
        'certificates': {
            'keywords': ['certificate', 'certification', 'certified', 'degree', 'diploma', 'credential', 'recognition', 'recognized', 'valid', 'government', 'accredited', 'authorized', 'completion certificate', 'course completion', 'industry recognized', 'iso', 'government certified', 'certificate value', 'will i get certificate', 'proof of completion'],
            'answer': """Every student receives a course completion certificate and a live project certificate. These certificates are industry-recognized and help in job applications."""
        },

        # ─────────────────────────────────────────────
        # 11. ELIGIBILITY
        # ─────────────────────────────────────────────
        'eligibility': {
            'keywords': ['eligibility', 'eligible', 'qualify', 'qualification', 'who can join', 'requirements', 'criteria', 'minimum', 'degree', 'student', 'fresher', 'beginner', 'experienced', 'professional', 'working', 'college', '12th', 'graduate', 'undergraduate', 'age', 'background', 'can i join', 'prerequisite', 'prior knowledge', 'anyone', 'no experience'],
            'answer': """Anyone can join - 10th/12th pass students, college students, fresh graduates, and working professionals. No prior coding experience is required for beginners."""
        },

        # ─────────────────────────────────────────────
        # 12. GENERAL FAQs
        # ─────────────────────────────────────────────
        'general_faq': {
            'keywords': ['demo', 'trial', 'free class', 'demo class', 'free demo', 'online', 'offline', 'mode', 'study material', 'notes', 'material', 'book', 'pdf', 'resources', 'doubt', 'doubt session', 'support after course', 'internship', 'what makes you different', 'why easylearn', 'unique', 'best institute', 'advantage', 'benefit', 'special', 'recording', 'recorded lecture', 'revision', 'faq', 'refund', 'cancellation', 'transfer', 'language', 'gujarati', 'hindi', 'english', 'medium'],
            'answer': """We offer free demo classes. Both online and offline training is available. Study material and recorded lectures are provided. We also give doubt support even after course completion. Teaching is done in Gujarati, Hindi, or English as needed."""
        }
    }
}