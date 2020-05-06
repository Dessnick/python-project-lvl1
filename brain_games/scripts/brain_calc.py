import brain_games.scripts.brain_games
from brain_games.driver import start


def main():
    greeting_calc = 'What is the result of the expression?'
    name = brain_games.scripts.brain_games.main(greeting_calc)
    start(name, 'calc')


if __name__ == '__main__':
    main()
