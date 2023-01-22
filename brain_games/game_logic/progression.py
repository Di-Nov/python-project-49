import random

START = 'What number is missing in the progression?'


def logic_function():
    count_elem = random.randint(5, 10)
    number_substitution = random.randint(1, count_elem)
    start_elem = random.randint(1, 100)
    arithmetic_progression_elem = random.randint(1, 10)
    question = []
    elem = 'error'
    for i in range(count_elem):
        if i == number_substitution-1:
            elem = start_elem
            question.append('..')
            start_elem += arithmetic_progression_elem
        elif i == 0:
            question.append(str(start_elem))
            start_elem += arithmetic_progression_elem
        else:
            question.append(str(start_elem))
            start_elem += arithmetic_progression_elem

    return ' '.join(question), str(elem)
