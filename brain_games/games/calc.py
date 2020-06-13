import operator
import random

GAME_RULES = 'What is the result of the expression?'
OPERATOR_FUNCTION_TUPLE = [('+', operator.add),
                           ('*', operator.mul),
                           ('-', operator.sub)]
MAX_NUMBER = 100


def start():
    number1 = random.randint(1, MAX_NUMBER)
    number2 = random.randint(1, MAX_NUMBER)
    oper_str, oper_func = random.choice(OPERATOR_FUNCTION_TUPLE)
    question = 'Question: {} {} {}'. format(number1, oper_str, number2)
    result = oper_func(number1, number2)
    return question, str(result)
