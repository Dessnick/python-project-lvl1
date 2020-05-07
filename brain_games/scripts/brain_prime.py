from brain_games.scripts.brain_games import greet_and_start


def main():
    greeting_prime = ('Answer "yes" if given number is prime. '
                      'Otherwise answer "no"')
    greet_and_start(greeting_prime, 'prime')


if __name__ == '__main__':
    main()
