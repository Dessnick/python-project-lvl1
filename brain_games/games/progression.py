from random import randint, randrange
GAME_RULES = 'What number is missing in the progression?'
MAX_NUMBER = 10


def start():
    prog_term = randint(1, MAX_NUMBER)
    difference = randint(1, MAX_NUMBER)
    series_length = MAX_NUMBER
    prog_array = []
    for i in range(1, series_length + 1):
        prog_array.append(prog_term)
        prog_term = prog_term + difference
    rand_index = randrange(len(prog_array))
    rand_term = prog_array[rand_index]
    prog_array[rand_index] = '..'
    question = 'Question: {}'. format(prog_string(prog_array))
    result = rand_term
    return (question, str(result))


def prog_string(array):
    array_str = ''
    for x in array:
        array_str += str(x) + ' '
    return array_str
