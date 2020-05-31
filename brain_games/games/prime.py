from random import randint
from math import sqrt
GAME_RULES = ('Answer "yes" if given number is prime. '
              'Otherwise answer "no"')


def start():
    number = randint(1, 100)
    question = 'Question: {}'. format(number)
    if number == 2:
        result = 'yes'
    elif number < 2:
        result = 'no'
    else:
        lim = int(sqrt(number))
        div = 2
        result = is_not_prime(div, lim, number)
    return (question, result)


def is_not_prime(div, lim, number):
    while(div <= lim):
        if number % div == 0:
            return 'no'
        div += 1
    return 'yes'
