from random import randint, randrange
from brain_games.cli import ask_prog
from brain_games.cli import user_answer
GAME_RULES = 'What number is missing in the progression?'


def start(name):
    prog_term = randint(1, 10)
    difference = randint(1, 10)
    series_length = 10
    prog_array = []
    for i in range(1, series_length + 1):
        prog_array.append(prog_term)
        prog_term = prog_term + difference
    rand_index = randrange(len(prog_array))
    rand_term = prog_array[rand_index]
    prog_array[rand_index] = '..'
    ask_prog(prog_array)
    answer = user_answer()
    result = rand_term
    if answer == str(result):
        print('Correct!')
        return True
    else:
        print("'{}'". format(answer) +
              " is wrong answer ;(. "
              "Correct answer was " + "'{}'". format(result) + ".")
        print("Let's try again, {}!". format(name))
        return False
