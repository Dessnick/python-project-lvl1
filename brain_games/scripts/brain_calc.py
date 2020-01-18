import brain_games.scripts.brain_games
from brain_games.cli import run
from brain_games.games.calc import game_calc


def main():
    brain_games.scripts.brain_games.main()
    print('What is the result of the expression?')
    print('')
    name = run()
    print('')
    game_calc(name)


if __name__ == '__main__':
    main()
