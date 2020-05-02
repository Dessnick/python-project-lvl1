from random import randrange
from brain_games.cli import ask_prog


def game_progression(prog_term, difference, series_length):
    prog_array = []
    for i in range(1, series_length + 1):
        prog_array.append(prog_term)
        prog_term = prog_term + difference
    rand_index = randrange(len(prog_array))
    rand_term = prog_array[rand_index]
    prog_array[rand_index] = '..'
    ask_prog(prog_array)
    return rand_term
