import prompt

import brain_games.games.calc
import brain_games.games.even
import brain_games.games.gcd
import brain_games.games.prime
import brain_games.games.progression
from brain_games.cli import welcome_and_get_user_name

GAMES_COUNT = 3


def play_game(game_name):
    match game_name:
        case 'even':
            game = brain_games.games.even
        case 'calc':
            game = brain_games.games.calc
        case 'gcd':
            game = brain_games.games.gcd
        case 'progression':
            game = brain_games.games.progression
        case 'prime':
            game = brain_games.games.prime
        case _:
            print('Unknown game')
            return

    user_name = welcome_and_get_user_name()

    print(game.get_introduction())

    for _ in range(GAMES_COUNT):
        question, correct_answer = game.get_round_task()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
