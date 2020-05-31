from operator import add, mul, sub
from random import randint, choice
GAME_RULES = 'What is the result of the expression?'
OPERATOR_FUNCTION_TUPLE = [('+', add), ('*', mul), ('-', sub)]
MAX_NUMBER = 100


def start():
    number1 = randint(1, MAX_NUMBER)
    number2 = randint(1, MAX_NUMBER)
    rand_calc = choice(OPERATOR_FUNCTION_TUPLE)
    question = 'Question: {} {} {}'. format(number1, rand_calc[0], number2)
    result = rand_calc[1](number1, number2)
    return question, str(result)
