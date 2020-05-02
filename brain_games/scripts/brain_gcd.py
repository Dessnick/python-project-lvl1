import brain_games.scripts.brain_games
from brain_games.cli import run
from brain_games.driver import start


def main():
    brain_games.scripts.brain_games.main()
    print('Find the greatest common divisor of given numbers.')
    print('')
    name = run()
    print('')
    start(name, 'gcd')


if __name__ == '__main__':
    main()
