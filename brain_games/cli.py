import prompt


def welcome_user(greeting_game):
    print('Welcome to the Brain Games!')
    if greeting_game != '':
        print(greeting_game)
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    print('')
    return name


def run():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    return name


def ask_num(number):
    print('Question: {}'. format(str(number)))
    return number


def ask_calc(number1, oper, number2):
    print('Question: {} {} {}'. format(str(number1), str(oper), str(number2)))


def ask_gcd(number1, number2):
    print('Question: {} {}'. format(str(number1), str(number2)))


def ask_prog(array):
    array_str = ''
    for x in array:
        array_str += str(x) + ' '
    print('Question: {}'. format(array_str))


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def wrong_answer(name, answer, correct_answer):
    print("'{}'". format(str(answer)) +
          " is wrong answer ;(. "
          "Correct answer was " + "'{}'". format(correct_answer) + ".")
    print("Let's try again, {}!". format(name))
