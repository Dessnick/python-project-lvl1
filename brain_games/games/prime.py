from random import randint
from math import sqrt
from brain_games.cli import ask_num
from brain_games.cli import user_answer
GAME_RULES = ('Answer "yes" if given number is prime. '
              'Otherwise answer "no"')


def start(name):
    number = randint(1, 100)
    ask_num(number)
    answer = user_answer()
    if number == 2:
        result = 'yes'
    elif number < 2:
        result = 'no'
    else:
        lim = int(sqrt(number))
        div = 2
        result = is_not_prime(div, lim, number)
    if answer == result:
        print('Correct!')
        return True
    else:
        print("'{}'". format(answer) +
              " is wrong answer ;(. "
              "Correct answer was " + "'{}'". format(result) + ".")
        print("Let's try again, {}!". format(name))
        return False


def is_not_prime(div, lim, number):
    while(div < lim):
        if number % div == 0:
            return 'no'
        div += 1
    return 'yes'
