import random

MAX_NUMBER = 20


def get_introduction():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_round_task():
    number = random.randint(1, MAX_NUMBER)

    question = str(number)
    answer = 'yes' if is_even(number) else 'no'

    return question, answer
