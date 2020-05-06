import brain_games.scripts.brain_games
# from brain_games.driver import start


def greet_and_play_gcd():
    greeting_gcd = 'Find the greatest common divisor of given numbers.'
    brain_games.scripts.brain_games.main(greeting_gcd, 'gcd')


def main():
    greet_and_play_gcd()
    # greeting_gcd = 'Find the greatest common divisor of given numbers.'
    # name = brain_games.scripts.brain_games.main(greeting_gcd)
    # start(name, 'even')


if __name__ == '__main__':
    main()
