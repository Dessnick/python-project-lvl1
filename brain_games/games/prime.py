import random
import math

GAME_RULES = ('Answer "yes" if given number is prime. '
              'Otherwise answer "no"')
MAX_NUMBER = 100


def start():
    number = random.randint(1, MAX_NUMBER)
    question = 'Question: {}'. format(number)
    if number == 2:
        result = True
    elif number < 2:
        result = False
    else:
        result = is_not_prime(number)
    return question, 'yes' if result else 'no'


def is_not_prime(number):
    lim = int(math.sqrt(number))
    div = 2
    while(div <= lim):
        if number % div == 0:
            return False
        div += 1
    return True
