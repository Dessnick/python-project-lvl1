import brain_games.scripts.brain_games
from brain_games.driver import start


def main():
    greeting_prime = ('Answer "yes" if given number is prime. '
                      + 'Otherwise answer "no"')
    name = brain_games.scripts.brain_games.main(greeting_prime)
    start(name, 'prime')


if __name__ == '__main__':
    main()
