import prompt


def run():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    return name


def ask_is_even(number):
    print('Question: {}'. format(str(number)))
    return number


def ask_calc(number1, oper, number2):
    print('Question: {} {} {}'. format(str(number1), str(oper), str(number2)))


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer
