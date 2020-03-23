from random import randint, choice
from brain_games.cli import ask_calc
from brain_games.cli import user_answer
from brain_games.cli import wrong_answer


def calc(number1, number2, oper):
    if oper == '-':
        return number1 - number2
    elif oper == '+':
        return number1 + number2
    elif oper == '*':
        return number1 * number2


def game_calc(name):
    counter = 0
    while counter < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        oper = choice('-+*')
        ask_calc(number1, oper, number2)
        answer = int(user_answer())
        calc_result = calc(number1, number2, oper)
        if (answer == calc_result):
            print('Correct!')
            counter = counter + 1
        else:
            wrong_answer(name, answer, calc_result)
            return

    print("Congratulations, {}!". format(name))