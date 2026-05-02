#Making a simple guess the number game

import random

print("Hello, what's your name?")
name = input()

print('Well, ' + name + ' ,I am thinking of a number between 1 to 20.')
secretNumber = random.randint(1,20)

for guesses in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Congrats! ' + name + ' , you guessed my number!')
else:
    print('No, the number I thought of was ' + str(secretNumber)+ '!')


print('You took ' + str(guesses) + ' guesses.')


