import prompt


def welcome_user(game_rules):
    print('Welcome to the Brain Games!')
    print(game_rules)
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    print('')
    return name


def ask_user(string):
    print('Question: {}'. format(string))


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer
