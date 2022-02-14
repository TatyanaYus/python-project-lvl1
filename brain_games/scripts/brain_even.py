"""Run brain games."""
from random import randint

import prompt

MAX_NUMBER = 10000


def main():
    """Welcome user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter < 3:
        number = randint(0, MAX_NUMBER)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')

        if number % 2 == 0 and answer == 'yes':
            print('Correct!')
            counter += 1
        elif number % 2 == 1 and answer == 'no':
            print('Correct!')
            counter += 1
        else:
            correct = 'yes' if number % 2 == 0 else 'no'

            wrong_answer = "'{0}' is wrong answer ;(. ".format(answer)
            try_again = "Correct answer was '{0}'.".format(correct)
            print(wrong_answer + try_again)

            print("Let's try again, {0}!".format(name))
            counter = 0
    print('Congratulations, {0}!'.format(name))


if __name__ == '__main__':
    main()
