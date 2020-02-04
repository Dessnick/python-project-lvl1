import brain_games.scripts.brain_games
from brain_games.cli import run
from brain_games.games.gcd import game_gcd


def main():
    brain_games.scripts.brain_games.main()
    print('Find the greatest common divisor of given numbers.')
    print('')
    name = run()
    print('')
    game_gcd(name)


if __name__ == '__main__':
    main()
