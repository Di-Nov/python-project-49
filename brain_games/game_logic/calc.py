from random import randint, choice
START = 'What is the result of the expression?'
MIN = 1
MAX = 100


def logic_function():
    random_number1 = randint(MIN, MAX)
    random_number2 = randint(MIN, MAX)
    random_elem = choice(['+', '-', '*'])
    return calculate_value(random_elem, random_number1, random_number2)


def calculate_value(re, rn1, rn2):
    result = 0
    operator = f'{rn1} {re} {rn2}'
    if re == '+':
        result = rn1 + rn2
    elif re == '-':
        result = rn1 - rn2
    elif re == '*':
        result = rn1 * rn2
    return operator, str(result)
