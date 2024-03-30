import random

MAX_NUMBER = 20
OPERATORS = '+', '-', '*'


def get_introduction():
    return 'What is the result of the expression?'


def calculate(operand_1, operand_2, operator):
    match operator:
        case '+':
            return operand_1 + operand_2
        case '-':
            return operand_1 - operand_2
        case '*':
            return operand_1 * operand_2
    return 'Unknown operator'


def get_round_task():
    operand_1 = random.randint(1, MAX_NUMBER)
    operand_2 = random.randint(1, MAX_NUMBER)
    if operand_2 > operand_1:
        operand_1, operand_2 = operand_2, operand_1
    operator = random.choice(OPERATORS)

    question = f'{operand_1} {operator} {operand_2}'
    answer = str(calculate(operand_1, operand_2, operator))

    return question, answer
