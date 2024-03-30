import random

MIN_COUNT = 5
MAX_COUNT = 10
MAX_START = 20
MIN_STEP = 2
MAX_STEP = 5


def get_introduction():
    return 'What number is missing in the progression?'


def get_progression(start, step, count):
    progression = []
    stop = start + (count - 1) * step
    for index in range(start, stop + 1, step):
        progression.append(str(index))
    return progression


def get_round_task():
    start = random.randint(1, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    count = random.randint(MIN_COUNT, MAX_COUNT)
    progression = get_progression(start, step, count)

    question_index = random.randint(1, count) - 1
    answer = progression[question_index]
    progression[question_index] = '..'
    question = ' '.join(progression)

    return question, answer
