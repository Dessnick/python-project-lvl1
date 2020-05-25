from random import randint
from brain_games.cli import ask_num
from brain_games.cli import user_answer
GAME_RULES = ('Answer "yes" if given number is prime. '
              'Otherwise answer "no"')


def start(name):
    number = randint(1, 100)
    ask_num(number)
    answer = user_answer()
    div = number - 1
    result = 'yes'
    while(div > 1):
        if number % div == 0:
            result = 'no'
        div = div - 1
    if answer == result:
        print('Correct!')
        return True
    else:
        print("'{}'". format(answer) +
              " is wrong answer ;(. "
              "Correct answer was " + "'{}'". format(result) + ".")
        print("Let's try again, {}!". format(name))
        return False
