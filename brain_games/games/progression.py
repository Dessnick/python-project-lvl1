from random import randint
from random import randrange
from brain_games.cli import ask_prog
from brain_games.cli import user_answer
from brain_games.cli import wrong_answer


def game_progression(name):
    counter = 0
    while counter < 3:
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
        answer = int(user_answer())

        if answer == rand_term:
            print('Correct!')
            counter = counter + 1
        else:
            wrong_answer(name, answer, rand_term)
            return

    print("Congratulations, {}!". format(name))
