from random import randint
from brain_games.cli import ask_num
from brain_games.cli import user_answer
from brain_games.cli import wrong_answer


def is_prime(number):
    if number == 1:
        return 'no'
    if number == 2:
        return 'yes'
    if number == 3:
        return 'yes'
    if (number % 2 == 0 or number % 3 == 0):
        return 'no'
    i = 5
    while(i * i <= number):
        if (number % i == 0 or number % (i + 2) == 0):
            return 'no'
        i = i + 6
    return 'yes'


def game_prime(name):
    counter = 0
    while counter < 3:
        number = ask_num(randint(1, 100))
        answer = user_answer()
        result = is_prime(number)
        if result == answer:
            print('Correct!')
            counter = counter + 1
        else:
            wrong_answer(name, answer, result)
            return

    print("Congratulations, {}!". format(name))
