from random import randint, choice

def welcome_message():
    return 'What is the result of the expression?'

def question():
    MAX_NUMBER = 100
    signs = ['+','-','*'] 
    
    number = randint(0, MAX_NUMBER) 
    sign = choice(signs)
    number2 = randint(0, MAX_NUMBER)
    print('Question: {0} {1} {2}'.format(number, sign, number2))


    if sign =='+':
        correct = number + number2
    elif sign == '-':
        correct = number - number2
    elif sign == '*':
        correct = number * number2 
    
    return str(correct)