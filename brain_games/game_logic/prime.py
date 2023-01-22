import random

START = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def logic_function():
    question = random.randint(2, 100)
    result = 'yes'
    for i in range(2, question):
        if question % i == 0:
            result = 'no'
            break
        else:
            result = 'yes'

    return question, result
