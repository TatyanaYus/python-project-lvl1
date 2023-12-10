from random import randint


def welcome_message():
    return 'Answer "yes" if the number is even, otherwise answer "no".'

def question():
    MAX_NUMBER = 10000
    number = randint(0, MAX_NUMBER)
    print('Question: {0}'.format(number))
    correct = 'yes' if number % 2 == 0 else 'no'
    return correct
