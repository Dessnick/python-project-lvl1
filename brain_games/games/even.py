from random import randint
from brain_games.cli import ask_is_even
from brain_games.cli import user_answer
from brain_games.cli import wrong_answer


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_even(name):
    counter = 0
    while counter < 3:
        number = ask_is_even(randint(1, 100))
        answer = user_answer()
        result = is_even(number)
        if answer == result:
            print('Correct!')
            counter = counter + 1
        else:
            wrong_answer(name, answer, result)
            return

    print("Congratulations, {}!". format(name))
