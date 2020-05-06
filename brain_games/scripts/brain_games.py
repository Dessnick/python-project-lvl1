from brain_games.cli import welcome_user
from brain_games.driver import start


def main(greeting_game, game):
    name = welcome_user(greeting_game)
    start(name, game)


if __name__ == '__main__':
    main()
