from random import randint
from math import gcd
from brain_games.cli import ask_gcd
from brain_games.cli import user_answer


def correct_answer(number1, number2, name, answer):
    gcd_result = gcd(number1, number2)
    if (answer == gcd_result):
        print('Correct!')
        return True
    else:
        print("'{}'". format(str(answer)) +
              " is wrong answer ;(. "
              "Correct answer was " + "'{}'". format(gcd_result) + ".")
        print("Let's try again, {}!". format(name))
        return False


def game_gcd(name):
    counter = 0
    while counter < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        ask_gcd(number1, number2)
        answer = int(user_answer())
        if correct_answer(number1, number2, name, answer):
            counter = counter + 1
        else:
            return

    print("Congratulations, {}!". format(name))
