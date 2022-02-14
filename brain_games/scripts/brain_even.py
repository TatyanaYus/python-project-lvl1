"""Run brain games."""
from brain_games.cli import welcome_user
from random import randint
import prompt

def main():
    """Welcome user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter < 3:
    	number = randint(0, 10000)
    	print('Question: ' + str(number))
    	answer = prompt.string('Your answer: ')

    	if number % 2 == 0 and answer == 'yes':
    		print('Correct!')
    		counter += 1
    	elif number % 2 == 1 and answer == 'no':
    		print('Correct!')
    		counter += 1
    	else:
    		correct = 'yes' if number % 2 == 0 else 'no'
    		print("'{}' is wrong answer ;(. Correct answer was '{}'. Let's try again, {}!".format(answer, correct, name))
    		counter = 0
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
