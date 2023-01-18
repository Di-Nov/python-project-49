import prompt
from brain_games.cli import welcome_user


def play_func(logic):
    name = welcome_user()
    print(logic.START)
    count = 0
    while count != 3:
        question, right_answer = logic.logic_function()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')

        if answer != right_answer:
            print(f'{answer} is wrong answer ;(. Correct answer was {right_answer} ')
            print(f"Let's try again, {name}!")
            count = 0

        else:
            print('Correct!')
            count += 1
    print(f'Congratulations, {name}!')
