from random import randint
import math

MAX_NUMBER = 20


def welcome_message():
    """welcome_message."""
    return 'Find the greatest common divisor of given numbers.'


def question():
    """question."""
    number = randint(0, MAX_NUMBER)
    number2 = randint(0, MAX_NUMBER)
    print('Question: {0} {1}'.format(number, number2))

    return str(func_gcd(number, number2))


def func_gcd(a, b):
	while a != 0 and b != 0:
		if a > b:
			a = a % b
		else:
			b = b % a

	return (a + b)
