import random

MAX_NUMBER = 20
OPERATORS = '+', '-', '*'


def get_introduction():
    return 'What is the result of the expression?'


def get_round_task():
    first_operand = random.randint(1, MAX_NUMBER)
    second_operand = random.randint(1, MAX_NUMBER)
    operator = random.choice(OPERATORS)
    question = f'{first_operand} {operator} {second_operand}'
    match operator:
        case '+':
            answer = first_operand + second_operand
        case '-':
            answer = first_operand - second_operand
        case '*':
            answer = first_operand * second_operand
        case _:
            answer = 'Unknown operator'
    return question, str(answer)
