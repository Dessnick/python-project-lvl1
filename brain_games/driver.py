from random import randint, choice
from brain_games.games.prime import is_prime
from brain_games.cli import ask_num
from brain_games.cli import ask_calc
from brain_games.cli import ask_gcd
from brain_games.cli import user_answer
from brain_games.cli import wrong_answer
from brain_games.games.calc import calc
from brain_games.games.even import is_even
from brain_games.games.gcd import gcd_result
from brain_games.games.progression import game_progression


def represent_answer(string):
    try:
        return int(string)
    except ValueError:
        return string


def start(name, game):
    counter = 0
    while counter < 3:
        result = run_game(game)
        answer = represent_answer(user_answer())
        if answer == result:
            print('Correct!')
            counter = counter + 1
        else:
            wrong_answer(name, answer, result)
            return

    print("Congratulations, {}!". format(name))


def run_game(game):
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    result = 0
    if game == 'calc':
        oper = choice('-+*')
        ask_calc(number1, oper, number2)
        result = calc(number1, number2, oper)
    elif game == 'even':
        ask_num(number1)
        result = is_even(number1)
    elif game == 'gcd':
        ask_gcd(number1, number2)
        result = gcd_result(number1, number2)
    elif game == 'prime':
        ask_num(1)
        result = is_prime(1)
    elif game == 'progression':
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        series_length = 10
        result = game_progression(number1, number2, series_length)
    return result
