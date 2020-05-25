from random import randint, choice
from brain_games.cli import ask_calc
from brain_games.cli import user_answer
GAME_RULES = 'What is the result of the expression?'


def start(name):
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    oper = choice('-+*')
    ask_calc(number1, oper, number2)
    if oper == '-':
        result = number1 - number2
    elif oper == '+':
        result = number1 + number2
    elif oper == '*':
        result = number1 * number2
    answer = user_answer()
    if answer == str(result):
        print('Correct!')
        return True
    else:
        print("'{}'". format(answer) +
              " is wrong answer ;(. "
              "Correct answer was " + "'{}'". format(result) + ".")
        print("Let's try again, {}!". format(name))
        return False
