from random import randint
START = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN = 1
MAX = 100


def logic_function():
    random_number = randint(MIN, MAX)

    return even_func(random_number)


def even_func(rn):
    result = 'no result'
    if rn % 2 == 0:
        result = 'yes'
    elif rn % 2 != 0:
        result = 'no'

    return rn, result
