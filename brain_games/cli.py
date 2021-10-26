"""Run brain games in cli."""
import prompt


def welcome_user():
    """Read a user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
