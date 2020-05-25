from brain_games.cli import welcome_user


def run(game):
    name = welcome_user(game.GAME_RULES)
    counter = 0
    while counter < 3:
        correct_answer = game.start(name)
        if correct_answer:
            counter = counter + 1
        else:
            return

    print("Congratulations, {}!". format(name))
