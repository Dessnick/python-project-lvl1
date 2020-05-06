import brain_games.scripts.brain_games
from brain_games.driver import start


def main():
    greeting_gcd = 'Find the greatest common divisor of given numbers.'
    name = brain_games.scripts.brain_games.main(greeting_gcd)
    start(name, 'even')


if __name__ == '__main__':
    main()
