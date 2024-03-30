import random

MIN_GCD = 2
MAX_NUMBER = 10


def get_introduction():
    return 'Find the greatest common divisor of given numbers.'


def calc_gcd(number_1, number_2):
    for divisor in range(min(number_1, number_2), 1, -1):
        if (number_1 % divisor == 0) and (number_2 % divisor == 0):
            return divisor
    return 1


def get_round_task():
    multiplier = random.randint(MIN_GCD, MAX_NUMBER)
    number_1 = random.randint(1, MAX_NUMBER) * multiplier
    number_2 = random.randint(1, MAX_NUMBER) * multiplier

    question = f'{number_1} {number_2}'
    answer = str(calc_gcd(number_1, number_2))

    return question, answer
