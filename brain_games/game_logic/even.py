from random import randint
START = 'Answer "yes" if the number is even, otherwise answer "no".'


def logic_function():
    random_number = randint(1, 100)
    result = 'error'
    if random_number % 2 == 0:
        result = 'yes'
    elif random_number % 2 != 0:
        result = 'no'
    return random_number, result