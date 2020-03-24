import brain_games.scripts.brain_games
from brain_games.cli import run
from brain_games.games.prime import game_prime


def main():
    brain_games.scripts.brain_games.main()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    print('')
    name = run()
    print('')
    game_prime(name)


if __name__ == '__main__':
    main()
