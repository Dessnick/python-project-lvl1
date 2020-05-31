from random import randint
GAME_RULES = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def start():
    number1 = randint(1, MAX_NUMBER)
    number2 = randint(1, MAX_NUMBER)
    question = 'Question: {} {}'. format(number1, number2)
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    result = number1 + number2
    return (question, str(result))
