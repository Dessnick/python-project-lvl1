import brain_games.scripts.brain_games
# from brain_games.driver import start


def greet_and_play_even():
    greeting_even = 'Find the greatest common divisor of given numbers.'
    brain_games.scripts.brain_games.main(greeting_even, 'even')


def main():
    greet_and_play_even()
    # greeting_even = 'Answer "yes" if number even otherwise answer "no".'
    # name = brain_games.scripts.brain_games.main(greeting_even)
    # start(name, 'even')


if __name__ == '__main__':
    main()
