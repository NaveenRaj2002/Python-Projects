import random

num = random.randint(1,100)

guesses = [0]

while True:
    guess = int(input("Guess a number between 1 to 100 \nWhats Your Guess? "))
    if guess <1 or guess >100:
        print("Invalid Number Please Guess Again!")
        continue

    if guess == num:
        print("Congratulation You Won the Game in {} attempts".format(len(guesses)))
        break

    guesses.append(guess)

    

    if guess > num:
        print("Your Guess is Higher")

    else:
        print("Your Guess is Lower")