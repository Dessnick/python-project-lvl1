from brain_games.cli import welcome_user, ask_user, user_answer


def run(game):
    name = welcome_user(game.GAME_RULES)
    counter = 0
    while counter < 3:
        question, correct_answer = game.start()
        ask_user(question)
        answer = user_answer()
        if correct_answer == answer:
            print('Correct!')
            counter = counter + 1
        else:
            print("'{}'". format(answer) +
                  " is wrong answer ;(. "
                  "Correct answer was " + "'{}'". format(correct_answer) + ".")
            print("Let's try again, {}!". format(name))
            return

    print("Congratulations, {}!". format(name))
