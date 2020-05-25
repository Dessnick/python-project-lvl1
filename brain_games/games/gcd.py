from random import randint
from brain_games.cli import ask_gcd
from brain_games.cli import user_answer
GAME_RULES = 'Find the greatest common divisor of given numbers.'


def start(name):
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    ask_gcd(number1, number2)
    answer = user_answer()
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    result = number1 + number2
    if answer == str(result):
        print('Correct!')
        return True
    else:
        print("'{}'". format(answer) +
              " is wrong answer ;(. "
              "Correct answer was " + "'{}'". format(result) + ".")
        print("Let's try again, {}!". format(name))
        return False
