import brain_games.scripts.brain_games
from brain_games.driver import start


def main():
    greeting_prog = 'What number is missing in the progression?'
    name = brain_games.scripts.brain_games.main(greeting_prog)
    start(name, 'progression')


if __name__ == '__main__':
    main()
