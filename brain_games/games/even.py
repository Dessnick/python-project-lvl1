from random import randint
GAME_RULES = 'Answer "yes" if number even otherwise answer "no".'


def start():
    number = randint(1, 100)
    question = 'Question: {}'. format(number)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return (question, result)
