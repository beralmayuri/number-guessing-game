import random
number = random.randint(1, 100)
attempts = 7
guessed = False
while attempts > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Correct! You got it 🎉")
        guessed = True
        break
    attempts = attempts - 1
if guessed == False:
    print("Game over! The number was", number)