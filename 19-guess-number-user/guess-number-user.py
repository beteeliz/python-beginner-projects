import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'\nGuess a number between 1 and {x}: '))
        if guess < random_number:
            print('\nSorry, guess again. The number is too low.')
        elif guess > random_number:
            print('\nSorry, guess again. The number is too high.')
    
    print(f'\nCongratulations! You guessed the number {random_number} correctly!')#

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'correct':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)').lower()

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # Could also be high because low = high
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    print('Congratulations! The computer guessed your number {guess} correctly!')

computer_guess(10)