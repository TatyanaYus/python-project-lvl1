from random import randint

MAX_NUMBER = 1000


def welcome_message():
    """welcome_message."""
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question():
    """question."""
    number = randint(0, MAX_NUMBER)
    print('Question: {0}'.format(number))

    return 'yes' if is_prime(number) else 'no'


def is_prime(number):
    if number == 2:
        return True
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
