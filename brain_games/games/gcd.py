from random import randint
from math import gcd
from brain_games.cli import ask_gcd
from brain_games.cli import user_answer
from brain_games.cli import wrong_answer


def game_gcd(name):
    counter = 0
    while counter < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        ask_gcd(number1, number2)
        answer = int(user_answer())
        gcd_result = gcd(number1, number2)
        if (answer == gcd_result):
            print('Correct!')
            counter = counter + 1
        else:
            wrong_answer(name, answer, gcd_result)
            return

    print("Congratulations, {}!". format(name))
