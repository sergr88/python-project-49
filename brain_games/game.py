import random

import prompt

from brain_games.cli import welcome_and_get_user_name

GAMES_COUNT = 3
MAX_NUMBER = 20


def is_even(number):
    return number % 2 == 0


def play_game():
    user_name = welcome_and_get_user_name()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(GAMES_COUNT):
        number = random.randint(1, MAX_NUMBER)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(number) else 'no'
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
