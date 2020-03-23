import brain_games.scripts.brain_games
from brain_games.cli import run
from brain_games.games.progression import game_progression


def main():
    brain_games.scripts.brain_games.main()
    print('What number is missing in the progression?')
    print('')
    name = run()
    print('')
    game_progression(name)


if __name__ == '__main__':
    main()
