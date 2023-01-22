from random import randint, choice
START = 'What is the result of the expression?'


def logic_function():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    random_elem = choice(['+', '-', '*'])
    operator = f'{random_number1} {random_elem} {random_number2}'
    result = 'error'
    if random_elem == '+':
        result = random_number1 + random_number2
    elif random_elem == '-':
        result = random_number1 - random_number2
    elif random_elem == '*':
        result = random_number1 * random_number2
    return operator, str(result)
