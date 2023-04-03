name = input("Type your sweet name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirty road, it has come to an end and you can go left or right. Which way did you like to go? ").lower()

if answer == 'left':
    answer = input("You come to a river, you can walk around it or swin accross? Type walk to walk around or swin to swim accross: ").lower()

    if answer == 'swim':
        print("You swim accross and you were eaten by Crocodile")

    elif answer == 'walk':
        print("You walk for many miles, ran out of water and you will loss the game")

    else:
        print("Not a valid option. You lose")

elif answer == 'right':
    answer = input("You come to a bridge, its look wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == 'back':
        print("You go back and lose")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stanger. Do you talk to them (yes,no) ").lower()

        if answer == 'yes':
            print("You talk to the stanger and they give you a gold. You Won!!!")

        elif answer == 'no':
            print("You ignore the stranger and they are offended, You Lose")

        else:
            print("Not a valid option. You lose")
        

    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose.")

print(f"Thank You for trying {name}")