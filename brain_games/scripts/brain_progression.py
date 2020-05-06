import brain_games.scripts.brain_games
# from brain_games.driver import start


def greet_and_play_prog():
    greeting_prog = 'What number is missing in the progression?'
    brain_games.scripts.brain_games.main(greeting_prog, 'progression')


def main():
    # greeting_prime = ('Answer "yes" if given number is prime. '
    #                   'Otherwise answer "no"')
    # brain_games.scripts.brain_games.main(greeting_prime, 'prime')
    # start(name, 'prime')
    greet_and_play_prog()

# def main():
#     greeting_prog = 'What number is missing in the progression?'
#     name = brain_games.scripts.brain_games.main(greeting_prog)
#     start(name, 'progression')


if __name__ == '__main__':
    main()
