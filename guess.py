#create a rand int
#input number
#if input < rand = 'too low'
#elif input > rand = 'too high'
#else: break
#if input == rand = 'sucess'

import random

secret = random.randint(1,20)
print('Guess a number. I am thinking of number 1 - 20. You have 6 guesses')
sisa = 6
for count in range(1,7):
    guess = input('What is your guess? ')
        
    if str(guess) == '':
        print('You are meant to input a number between 1 -20, try again')
        break

    guess = int(guess)

    if guess < secret:
        print('Unfortunate, your number is too low')
        sisa = sisa - 1
        print('{} guesses left'.format(sisa))    
    elif guess > secret:
        print('Unfortunate, your number is too high')      
        sisa = sisa - 1
        print('{} guesses left'.format(sisa))  
    elif guess == secret:
        print('Congratulation, you have guessed the right number!')
        break
