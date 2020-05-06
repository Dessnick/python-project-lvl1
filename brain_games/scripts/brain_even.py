import brain_games.scripts.brain_games
from brain_games.driver import start


def main():
    greeting_even = 'Answer "yes" if number even otherwise answer "no".'
    name = brain_games.scripts.brain_games.main(greeting_even)
    start(name, 'even')


if __name__ == '__main__':
    main()
