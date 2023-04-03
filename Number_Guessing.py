import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(1, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess. You have only 5 chance to guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Your guess is higher")
    else:
        print("Your guess is lower")
    if guesses == 5:
        print("Your chance got over! Better luck next time")
        quit()