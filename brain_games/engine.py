import brain_games.cli as cli


def run(game, rounds=3):
    name = cli.welcome_user(game.GAME_RULES)
    counter = 0
    while counter < rounds:
        question, correct_answer = game.start()
        print(question)
        answer = cli.user_answer()
        if correct_answer == answer:
            print('Correct!')
            counter = counter + 1
        else:
            print("'{}' is wrong answer ;(."
                  "Correct answer was '{}'.". format(answer, correct_answer))
            print("Let's try again, {}!". format(name))
            return

    print("Congratulations, {}!". format(name))
