print("welcome to my computer quiz")

playing = input("Do you want to play? Type YES or NO: ").upper()
if playing != "YES":
    quit()

print("Okay! Let's Play :)")
score = 0
answer1 = input("What does CPU stands for? ").lower()
if answer1 == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'central processing unit'")

answer2 = input("what does GPU stands for? ").lower()
if answer2 == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'graphics processing unit'")

answer3 = input("What does RAM stands for? ").lower()
if answer3 == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'random access memory'")

answer4 = input("What does PSU stands for? ").lower()
if answer4 == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'power supply'")

answer5 = input("What does ROM stands for? ").lower()
if answer5 == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is 'read only memory'")

print(f"You got {score} question correct!")

print(f"You got {((score / 5) * 100)}%")