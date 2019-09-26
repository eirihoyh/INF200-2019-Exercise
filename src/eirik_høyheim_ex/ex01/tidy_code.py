from random import randint as rand

__author__ = 'Eirik Høyheim'
__email__ = 'eirihoyh@nmbu.no'


def number_guess():
    """
    Askes 'your guess' and remember the guess
    """
    your_number = 0
    while your_number < 1:
        your_number = int(input('Your guess: '))
    return your_number


def random_number():
    """
    Makes two random numbers between 1 and 6 and
    adds them together
    """
    return rand(1, 6) + rand(1, 6)


def number_comparison(number_guess, random_number):
    """
    Compares two given numbers and checks if they are the same number
    """
    return number_guess == random_number


if __name__ == '__main__':

    pre_answer = False
    chances = 3
    correct_number = random_number()
    while not pre_answer and chances > 0:  
        my_guess = number_guess()
        pre_answer = number_comparison(correct_number, my_guess)
        if not pre_answer:
            print('Wrong, try again!')
            chances -= 1

    if chances > 0:
        print('You won {} points.'.format(chances))
    else:
        print('You lost. Correct answer: {}.'.format(correct_number))
