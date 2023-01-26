import random
START = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUM = 100
MIN_NUM = 2


def logic_function():
    question = random.randint(MIN_NUM, MAX_NUM)

    return question, prime_func(question)


def prime_func(q):
    result = 'yes'
    for i in range(MIN_NUM, q):
        if q % i == 0:
            result = 'no'
            break
        else:
            result = 'yes'
    return result
