from random import randint

MAX_NUMBER = 10000


def welcome_message():
    """welcome_message."""
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    """question."""
    number = randint(0, MAX_NUMBER)
    print('Question: {0}'.format(number))

    return 'yes' if number % 2 == 0 else 'no'
