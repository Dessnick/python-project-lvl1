import brain_games.scripts.brain_games
from brain_games.cli import run
from brain_games.driver import start


def main():
    brain_games.scripts.brain_games.main()
    print('What is the result of the expression?')
    print('')
    name = run()
    print('')
    start(name, 'calc')


if __name__ == '__main__':
    main()
