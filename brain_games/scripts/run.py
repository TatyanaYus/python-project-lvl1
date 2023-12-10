"""Run brain games."""

import prompt
from brain_games.games import even, calc


def brain_even():
    main(even.welcome_message, even.question)

def brain_calc():
    main(calc.welcome_message, calc.question)


def main(welcome_message, question):
    """Welcome user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    print(welcome_message())

    counter = 0
    while counter < 3:
        correct = question() 

        answer = prompt.string('Your answer: ')

        if correct == answer:
            print('Correct!')
            counter += 1 
        else:
            wrong_answer = "'{0}' is wrong answer ;(. ".format(answer)
            try_again = "Correct answer was '{0}'.".format(correct)
            print(wrong_answer + try_again)

            print("Let's try again, {0}!".format(name))
            counter = 0
    print('Congratulations, {0}!'.format(name))


if __name__ == '__main__':
    main()
