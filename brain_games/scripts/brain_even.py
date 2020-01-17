import brain_games.scripts.brain_games
from brain_games.cli import run
from brain_games.even import game_even


def main():
    brain_games.scripts.brain_games.main()
    print('Answer "yes" if number even otherwise answer "no".')
    print('')
    name = run()
    print('')
    game_even(name)


if __name__ == '__main__':
    main()
