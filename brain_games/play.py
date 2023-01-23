import prompt
from brain_games.cli import welcome_user


def play_func(logic):
    name = welcome_user()
    print(logic.START)
    count = 0
    for _ in range(3):
        question, right_answer = logic.logic_function()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')

        if answer != right_answer:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {right_answer} ')
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            count += 1
    if count == 3:
        print(f'Congratulations, {name}!')
