# fiction-quiz/universe/hogwarts/main.py

QUESTIONS = {
    "q1": {
        "text": "What defines you most?",
        "options": {
            "A": {"label": "Courage",       "categories": ["gryffindor"]},
            "B": {"label": "Ambition",      "categories": ["slytherin"]},
            "C": {"label": "Intelligence",  "categories": ["ravenclaw"]},
            "D": {"label": "Loyalty",       "categories": ["hufflepuff"]}
        }
    },
    "q2": {
        "text": "Your ideal role?",
        "options": {
            "A": {"label": "Leader",        "categories": ["gryffindor"]},
            "B": {"label": "Strategist",    "categories": ["slytherin"]},
            "C": {"label": "Scholar",       "categories": ["ravenclaw"]},
            "D": {"label": "Supporter",     "categories": ["hufflepuff"]}
        }
    },
    "q3": {
        "text": "Biggest strength?",
        "options": {
            "A": {"label": "Bravery",       "categories": ["gryffindor"]},
            "B": {"label": "Determination", "categories": ["slytherin"]},
            "C": {"label": "Creativity",    "categories": ["ravenclaw"]},
            "D": {"label": "Kindness",      "categories": ["hufflepuff"]}
        }
    },
    "q4": {
        "text": "Biggest weakness?",
        "options": {
            "A": {"label": "Reckless",      "categories": ["gryffindor"]},
            "B": {"label": "Manipulative",  "categories": ["slytherin"]},
            "C": {"label": "Overthinking",  "categories": ["ravenclaw"]},
            "D": {"label": "Too trusting",  "categories": ["hufflepuff"]}
        }
    },
    "q5": {
        "text": "Favorite subject?",
        "options": {
            "A": {"label": "Defense Against Dark Arts", "categories": ["gryffindor"]},
            "B": {"label": "Potions",                   "categories": ["slytherin"]},
            "C": {"label": "Charms",                    "categories": ["ravenclaw"]},
            "D": {"label": "Herbology",                 "categories": ["hufflepuff"]}
        }
    },
    "q6": {
        "text": "How do you handle conflict?",
        "options": {
            "A": {"label": "Face it head-on", "categories": ["gryffindor"]},
            "B": {"label": "Outsmart",         "categories": ["slytherin"]},
            "C": {"label": "Analyze",          "categories": ["ravenclaw"]},
            "D": {"label": "Avoid harm",       "categories": ["hufflepuff"]}
        }
    },
    "q7": {
        "text": "Pick a trait:",
        "options": {
            "A": {"label": "Bold",    "categories": ["gryffindor"]},
            "B": {"label": "Cunning", "categories": ["slytherin"]},
            "C": {"label": "Curious", "categories": ["ravenclaw"]},
            "D": {"label": "Patient", "categories": ["hufflepuff"]}
        }
    },
    "q8": {
        "text": "Your friend group sees you as:",
        "options": {
            "A": {"label": "Protector",  "categories": ["gryffindor"]},
            "B": {"label": "Planner",    "categories": ["slytherin"]},
            "C": {"label": "Brain",      "categories": ["ravenclaw"]},
            "D": {"label": "Caretaker",  "categories": ["hufflepuff"]}
        }
    },
    "q9": {
        "text": "What matters most?",
        "options": {
            "A": {"label": "Honor",      "categories": ["gryffindor"]},
            "B": {"label": "Success",    "categories": ["slytherin"]},
            "C": {"label": "Knowledge",  "categories": ["ravenclaw"]},
            "D": {"label": "Friendship", "categories": ["hufflepuff"]}
        }
    },
    "q10": {
        "text": "Your vibe?",
        "options": {
            "A": {"label": "Fearless",    "categories": ["gryffindor"]},
            "B": {"label": "Calculated",  "categories": ["slytherin"]},
            "C": {"label": "Thoughtful",  "categories": ["ravenclaw"]},
            "D": {"label": "Warm",        "categories": ["hufflepuff"]}
        }
    }
}

def run_quiz(form_data):
    """
    form_data = request.form from Flask
    """

    score = {
        "gryffindor": 0,
        "slytherin": 0,
        "ravenclaw": 0,
        "hufflepuff": 0
    }

    for q, data in QUESTIONS.items():
        answer = form_data.get(q)
        if answer and answer in data["options"]:
            for category in data["options"][answer]["categories"]:
                score[category] += 1

    result = max(score, key=score.get)
    return result