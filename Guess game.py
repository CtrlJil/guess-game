from random import randint

numberToGuess = randint(1, 100)
userGuess = -1

while numberToGuess != userGuess:
    userGuess = int(input("Enter a number: "))
    if numberToGuess > userGuess:
        print("Higher!")
    elif numberToGuess < userGuess:
        print("Lower!")
print("You win!")