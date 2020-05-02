import brain_games.scripts.brain_games
from brain_games.cli import run
from brain_games.driver import start


def main():
    brain_games.scripts.brain_games.main()
    print('Answer "yes" if number even otherwise answer "no".')
    print('')
    name = run()
    print('')
    start(name, 'even')


if __name__ == '__main__':
    main()
