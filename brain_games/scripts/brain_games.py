from brain_games.cli import welcome_user
from brain_games.driver import start


def greet_and_start(greeting_game, game):
    name = welcome_user(greeting_game)
    start(name, game)


def main():
    welcome_user('')


if __name__ == '__main__':
    main()
