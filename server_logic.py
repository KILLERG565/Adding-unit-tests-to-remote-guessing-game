import random

def generate_random(difficulty):
    if difficulty == 1:
        return random.randint(1, 10)
    elif difficulty == 2:
        return random.randint(1, 50)
    return random.randint(1, 100)

def get_difficulty_message():
    return """
    Difficulty
    ==========
    1) easy
    2) medium 
    3) hard
    enter choice:"""

def parse_guess(data):
    try:
        return int(data.strip())
    except ValueError:
        return None

def evaluate_guess(secret, guess):
    if guess == secret:
        return "CORRECT!"
    elif guess > secret:
        return "=Guess Lower\nenter guess: "
    else:
        return "=Guess Higher\nenter guess: "
# the servers function 