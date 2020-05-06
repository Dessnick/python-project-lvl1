import brain_games.scripts.brain_games
# from brain_games.driver import start


def greet_and_play_prime():
    greeting_prime = ('Answer "yes" if given number is prime. '
                      'Otherwise answer "no"')
    brain_games.scripts.brain_games.main(greeting_prime, 'prime')


def main():
    # greeting_prime = ('Answer "yes" if given number is prime. '
    #                   'Otherwise answer "no"')
    # brain_games.scripts.brain_games.main(greeting_prime, 'prime')
    # start(name, 'prime')
    greet_and_play_prime()


if __name__ == '__main__':
    main()
