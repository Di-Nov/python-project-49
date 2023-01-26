import random
START = 'Find the greatest common divisor of given numbers.'
MIN = 1
MAX = 100


def logic_function():
    number_1 = random.randint(MIN, MAX)
    number_2 = random.randint(MIN, MAX)
    max_num, min_num = max(number_1, number_2), min(number_1, number_2)

    return f'{number_1} {number_2}', gcd_func(max_num, min_num)


def gcd_func(max_n, min_n):
    result = 0
    for i in range(min_n, 0, -1):
        if min_n % i == 0 and max_n % i == 0:
            result = i
            break

    return str(result)
