import random

lower = 1
upper = 100

magic_number = random.randint(lower, upper)

guess = int(input('Guess a number between %d and %d' % (lower, upper)))
number_of_guesses = 1

while True:

    guess = int(input('What is your next guess? '))
    number_of_guesses += 1

    if guess > magic_number:
        print('lower ...')

    elif guess < magic_number:
        print('higher ...')

    else:
        print(f'YEAAAH!!!! You guessed it in {number_of_guesses} guesses')
        break
