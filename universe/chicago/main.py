# fiction-quiz/universe/chicago/main.py

QUESTIONS = {
        "q1": {
            "text": "You value:",
            "options": {
                "A": {"label": "Selflessness", "categories": ["abnegation"]},
                "B": {"label": "Bravery",      "categories": ["dauntless"]},
                "C": {"label": "Knowledge",    "categories": ["erudite"]},
                "D": {"label": "Peace",        "categories": ["amity"]},
                "E": {"label": "Honesty",      "categories": ["candor"]}
            }
        },
        "q2": {
            "text": "Your ideal life:",
            "options": {
                "A": {"label": "Helping others",   "categories": ["abnegation"]},
                "B": {"label": "Thrill and action", "categories": ["dauntless"]},
                "C": {"label": "Learning",          "categories": ["erudite"]},
                "D": {"label": "Harmony",           "categories": ["amity"]},
                "E": {"label": "Truth",             "categories": ["candor"]}
            }
        },
        "q3": {
            "text": "Fear response:",
            "options": {
                "A": {"label": "Stay calm", "categories": ["abnegation"]},
                "B": {"label": "Confront",  "categories": ["dauntless"]},
                "C": {"label": "Analyze",   "categories": ["erudite"]},
                "D": {"label": "Avoid",     "categories": ["amity"]},
                "E": {"label": "Admit",     "categories": ["candor"]}
            }
        },
        "q4": {
            "text": "What motivates you?",
            "options": {
                "A": {"label": "Duty",       "categories": ["abnegation"]},
                "B": {"label": "Adrenaline", "categories": ["dauntless"]},
                "C": {"label": "Curiosity",  "categories": ["erudite"]},
                "D": {"label": "Happiness",  "categories": ["amity"]},
                "E": {"label": "Integrity",  "categories": ["candor"]}
            }
        },
        "q5": {
            "text": "Your weakness:",
            "options": {
                "A": {"label": "Self-neglect", "categories": ["abnegation"]},
                "B": {"label": "Impulsive",    "categories": ["dauntless"]},
                "C": {"label": "Arrogant",     "categories": ["erudite"]},
                "D": {"label": "Passive",      "categories": ["amity"]},
                "E": {"label": "Blunt",        "categories": ["candor"]}
            }
        },
        "q6": {
            "text": "Social role:",
            "options": {
                "A": {"label": "Caregiver",    "categories": ["abnegation"]},
                "B": {"label": "Risk-taker",   "categories": ["dauntless"]},
                "C": {"label": "Thinker",      "categories": ["erudite"]},
                "D": {"label": "Peacemaker",   "categories": ["amity"]},
                "E": {"label": "Truth-teller", "categories": ["candor"]}
            }
        },
        "q7": {
            "text": "Choose:",
            "options": {
                "A": {"label": "Sacrifice", "categories": ["abnegation"]},
                "B": {"label": "Courage",   "categories": ["dauntless"]},
                "C": {"label": "Logic",     "categories": ["erudite"]},
                "D": {"label": "Kindness",  "categories": ["amity"]},
                "E": {"label": "Honesty",   "categories": ["candor"]}
            }
        },
        "q8": {
            "text": "Conflict style:",
            "options": {
                "A": {"label": "Yield",       "categories": ["abnegation"]},
                "B": {"label": "Fight",       "categories": ["dauntless"]},
                "C": {"label": "Debate",      "categories": ["erudite"]},
                "D": {"label": "Mediate",     "categories": ["amity"]},
                "E": {"label": "Speak truth", "categories": ["candor"]}
            }
        },
        "q9": {
            "text": "Ideal job:",
            "options": {
                "A": {"label": "Volunteer",  "categories": ["abnegation"]},
                "B": {"label": "Soldier",    "categories": ["dauntless"]},
                "C": {"label": "Scientist",  "categories": ["erudite"]},
                "D": {"label": "Farmer",     "categories": ["amity"]},
                "E": {"label": "Lawyer",     "categories": ["candor"]}
            }
        },
        "q10": {
            "text": "You are:",
            "options": {
                "A": {"label": "Selfless",     "categories": ["abnegation"]},
                "B": {"label": "Fearless",     "categories": ["dauntless"]},
                "C": {"label": "Intelligent",  "categories": ["erudite"]},
                "D": {"label": "Gentle",       "categories": ["amity"]},
                "E": {"label": "Honest",       "categories": ["candor"]}
            }
        }
    }

def run_quiz(form_data):
    """
    form_data = request.form from Flask
    """

    score = {
        "abnegation": 0,
        "dauntless": 0,
        "erudite": 0,
        "amity": 0,
        "candor": 0
    }

    for q, data in QUESTIONS.items():
        answer = form_data.get(q)
        if answer and answer in data["options"]:
            for category in data["options"][answer]["categories"]:
                score[category] += 1

    result = max(score, key=score.get)
    return result