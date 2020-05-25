import prompt


def welcome_user(game_rules):
    print('Welcome to the Brain Games!')
    if game_rules != '':
        print(game_rules)
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    print('')
    return name


def ask_num(number):
    print('Question: {}'. format(number))
    return number


def ask_calc(number1, oper, number2):
    print('Question: {} {} {}'. format(number1, oper, number2))


def ask_gcd(number1, number2):
    print('Question: {} {}'. format(number1, number2))


def ask_prog(array):
    array_str = ''
    for x in array:
        array_str += str(x) + ' '
    print('Question: {}'. format(array_str))


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer
