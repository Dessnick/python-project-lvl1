from random import randint
from brain_games.cli import ask_is_even
from brain_games.cli import user_answer


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def correct_answer(answer, number, name):
    if (answer == 'yes' and is_even(number) == 'yes') \
            or (answer == 'no' and is_even(number) == 'no'):
        print('Correct!')
        return True
    else:
        print("'{}'". format(str(answer)) +
              " is wrong answer ;(. "
              "Correct answer was " + "'{}'". format(is_even(number)) + ".")
        print("Let's try again, {}!". format(name))
        return False


def game_even(name):
    counter = 0
    while counter < 3:
        number = ask_is_even(randint(1, 100))
        answer = user_answer()
        if correct_answer(answer, number, name):
            counter = counter + 1
        else:
            return

    print("Congratulations, {}!". format(name))
