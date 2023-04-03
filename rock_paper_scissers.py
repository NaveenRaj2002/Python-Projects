import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Not a valid input! TYPE AGAIN CORRECTLY!!!")
        continue

    random_number = random.randint(0,2)
    # 0 as rock
    # 1 as paper
    # 2 as scissors

    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        
    elif user_input == computer_pick:
        print("TIED")

    else:
        print("You lost!")
        computer_wins += 1
    
print(f"You Won {user_wins} times")
print(f"The Computer Won {computer_wins} times")
print("Goodbye!")