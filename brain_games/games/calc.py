from random import choice, randint

MAX_NUMBER = 100
signs = ['+', '-', '*']


def welcome_message():
    """welcome_message."""
    return 'What is the result of the expression?'


def question():
    """question."""
    number = randint(0, MAX_NUMBER)
    sign = choice(signs)
    number2 = randint(0, MAX_NUMBER)
    print('Question: {0} {1} {2}'.format(number, sign, number2))

    if sign == '+':
        correct = number + number2
    elif sign == '-':
        correct = number - number2
    elif sign == '*':
        correct = number * number2
    return str(correct)
