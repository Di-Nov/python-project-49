import prompt
from brain_games.cli import welcome_user
from random import randint


def even_number():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer ("yes" or "no"): ')
        while answer not in ['yes', 'no']:
            print('please enter answer only "yes" or "no"')
            answer = prompt.string('Your answer ("yes" or "no"): ')
        unanswer = 'no' if answer == 'yes' else 'yes'
        if answer == 'yes' and random_number % 2 != 0 or answer == 'no' and random_number % 2 == 0:
            print(f'{answer} is wrong answer ;(. Correct answer was {unanswer} ')
            print(f"Let's try again, {name}!")
            count = 0

        else:
            print('Correct!')
            count += 1
    print(f'Congratulations, {name}!')