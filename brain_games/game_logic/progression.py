import random
START = 'What number is missing in the progression?'
MIN_PROGRESSION = 5
MAX_PROGRESSION = 10
MIN_ELEM = 1
MAX_ELEM = 50

def logic_function():
    count_elem = random.randint(MIN_PROGRESSION, MAX_PROGRESSION)
    index_substitution = random.randint(1, count_elem)
    start_elem = random.randint(MIN_ELEM, MAX_ELEM)
    arithmetic_progression_elem = random.randint(MIN_ELEM, MAX_ELEM)

    return progression_func(count_elem, index_substitution, start_elem, arithmetic_progression_elem)


def progression_func(count_elem, index_substitution, start_elem, arithmetic_progression_elem):
    question = []
    for i in range(count_elem):
        if i == index_substitution - 1:
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
