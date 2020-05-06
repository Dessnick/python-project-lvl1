import brain_games.scripts.brain_games
# from brain_games.driver import start


def greet_and_play_calc():
    greeting_calc = 'What is the result of the expression?'
    brain_games.scripts.brain_games.main(greeting_calc, 'calc')


def main():
    # greeting_calc = 'What is the result of the expression?'
    # name = brain_games.scripts.brain_games.main(greeting_calc)
    # start(name, 'calc')
    greet_and_play_calc()


if __name__ == '__main__':
    main()
