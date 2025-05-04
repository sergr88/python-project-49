import math
import random

MIN_NUMBER = 2
MAX_NUMBER = 20


def get_introduction():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    square_root = math.sqrt(number)
    return all(number % divisor != 0
               for divisor in range(2, math.floor(square_root) + 1))


def get_round_task():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'

    return question, answer
