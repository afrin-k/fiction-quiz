# fiction-quiz/universe/olympus/main.py

QUESTIONS = {
    "q1": {
        "text": "Your power would be:",
        "options": {
            "A": {"label": "Lightning",  "categories": ["zeus", "apollo"]},
            "B": {"label": "Water",      "categories": ["poseidon", "demeter"]},
            "C": {"label": "Shadows",    "categories": ["hades", "hermes"]},
            "D": {"label": "Fire/Craft", "categories": ["hephaestus", "ares"]}
        }
    },
    "q2": {
        "text": "Your personality:",
        "options": {
            "A": {"label": "Leader",    "categories": ["zeus", "ares"]},
            "B": {"label": "Calm",      "categories": ["poseidon", "demeter"]},
            "C": {"label": "Reserved",  "categories": ["hades", "athena"]},
            "D": {"label": "Creative",  "categories": ["hephaestus", "apollo"]}
        }
    },
    "q3": {
        "text": "You enjoy:",
        "options": {
            "A": {"label": "Winning",        "categories": ["ares", "zeus"]},
            "B": {"label": "Love/socializing","categories": ["aphrodite", "dionysus"]},
            "C": {"label": "Music/art",      "categories": ["apollo", "aphrodite"]},
            "D": {"label": "Thinking",       "categories": ["athena", "hades"]}
        }
    },
    "q4": {
        "text": "Your strength:",
        "options": {
            "A": {"label": "Combat",    "categories": ["ares", "zeus"]},
            "B": {"label": "Charm",     "categories": ["aphrodite", "hermes"]},
            "C": {"label": "Talent",    "categories": ["apollo", "dionysus"]},
            "D": {"label": "Strategy",  "categories": ["athena", "hades"]}
        }
    },
    "q5": {
        "text": "Your weakness:",
        "options": {
            "A": {"label": "Pride",       "categories": ["zeus", "ares"]},
            "B": {"label": "Mood swings", "categories": ["poseidon", "dionysus"]},
            "C": {"label": "Isolation",   "categories": ["hades", "athena"]},
            "D": {"label": "Obsession",   "categories": ["hephaestus", "apollo"]}
        }
    },
    "q6": {
        "text": "Ideal activity:",
        "options": {
            "A": {"label": "Exploring", "categories": ["hermes", "apollo"]},
            "B": {"label": "Nature",    "categories": ["demeter", "poseidon"]},
            "C": {"label": "Partying",  "categories": ["dionysus", "aphrodite"]},
            "D": {"label": "Training",  "categories": ["ares", "zeus"]}
        }
    },
    "q7": {
        "text": "People see you as:",
        "options": {
            "A": {"label": "Fast",   "categories": ["hermes", "apollo"]},
            "B": {"label": "Caring", "categories": ["demeter", "aphrodite"]},
            "C": {"label": "Fun",    "categories": ["dionysus", "hermes"]},
            "D": {"label": "Strong", "categories": ["ares", "zeus"]}
        }
    },
    "q8": {
        "text": "Your vibe:",
        "options": {
            "A": {"label": "Sky",        "categories": ["zeus", "apollo"]},
            "B": {"label": "Ocean",      "categories": ["poseidon", "demeter"]},
            "C": {"label": "Underworld", "categories": ["hades", "athena"]},
            "D": {"label": "Fire",       "categories": ["hephaestus", "ares"]}
        }
    },
    "q9": {
        "text": "What matters most:",
        "options": {
            "A": {"label": "Power",    "categories": ["zeus", "ares"]},
            "B": {"label": "Balance",  "categories": ["poseidon", "demeter"]},
            "C": {"label": "Control",  "categories": ["hades", "athena"]},
            "D": {"label": "Creation", "categories": ["hephaestus", "apollo"]}
        }
    },
    "q10": {
        "text": "You prefer:",
        "options": {
            "A": {"label": "Leadership", "categories": ["zeus", "ares"]},
            "B": {"label": "Peace",      "categories": ["demeter", "poseidon"]},
            "C": {"label": "Wisdom",     "categories": ["athena", "hades"]},
            "D": {"label": "Expression", "categories": ["apollo", "dionysus"]}
        }
    }
}

def run_quiz(form_data):
    """
    form_data = request.form from Flask
    """

    score = {
        "zeus": 0,
        "poseidon": 0,
        "hades": 0,
        "ares": 0,
        "aphrodite": 0,
        "apollo": 0,
        "hephaestus": 0,
        "athena": 0,
        "hermes": 0,
        "demeter": 0,
        "dionysus": 0
    }


    for q, data in QUESTIONS.items():
        answer = form_data.get(q)
        if answer and answer in data["options"]:
            for category in data["options"][answer]["categories"]:
                score[category] += 1

    result = max(score, key=score.get)
    return result