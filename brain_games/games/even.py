import random

GAME_RULES = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUMBER = 100


def start():
    number = random.randint(1, MAX_NUMBER)
    question = 'Question: {}'. format(number)
    return question, 'yes' if number % 2 == 0 else 'no'
