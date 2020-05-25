from random import randint
from brain_games.cli import ask_num
from brain_games.cli import user_answer
GAME_RULES = 'Find the greatest common divisor of given numbers'


def start(name):
    number = randint(1, 100)
    ask_num(number)
    answer = user_answer()
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    if answer == result:
        print('Correct!')
        return True
    else:
        print("'{}'". format(answer) +
              " is wrong answer ;(. "
              "Correct answer was " + "'{}'". format(result) + ".")
        print("Let's try again, {}!". format(name))
        return False
