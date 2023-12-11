from random import randint

MAX_NUMBER_START = 20
MAX_NUMBER_STEP = 10


def welcome_message():
    """welcome_message."""
    return 'What number is missing in the progression?'


def question():
    """question."""
    start = randint(0, MAX_NUMBER_START)
    step = randint(1, MAX_NUMBER_STEP)
    lenght = randint(5, 10)
    end = start + (lenght - 1) * step
    position = randint(0, lenght - 1)
    progres = arifmetic_progression(start, end, step)
    correct = progres[position]
    progres[position] = '..'
    print('Question: {0}'.format(' '.join(map(str, progres))))

    return str(correct)


def arifmetic_progression(start, end, step):
    """arifmetic_progression."""
    return list(range(start, end + 1, step))
