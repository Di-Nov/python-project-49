import random

START = 'Find the greatest common divisor of given numbers.'


def logic_function():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    max_num, min_num = max(number_1, number_2), min(number_1, number_2)
    result = 0
    for i in range(min_num, 0, -1):
        if min_num % i == 0 and max_num % i == 0:
            result = i
            break

    return f'{number_1} {number_2}', str(result)

