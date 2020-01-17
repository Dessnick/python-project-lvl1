import prompt


def run():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    return name


def ask_is_even(number):
    print('Question: {}'. format(str(number)))
    return number


def answer_is_even():
    answer = prompt.string('Your answer: ')
    return answer
