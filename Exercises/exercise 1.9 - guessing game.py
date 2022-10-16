import random

lower = 1
upper = 100

magic_number = random.randint(lower, upper)

guess = int(input('Guess a number between %d and %d' % (lower, upper)))
number_of_guesses = 1

while guess != magic_number:

    if guess > magic_number:
        print('lower ...')

    else:
        print('higher ...')

    guess = int(input('What is your next guess? '))
    number_of_guesses += 1


print(f'YEAAAH!!!! You guessed it in {number_of_guesses} guesses')
