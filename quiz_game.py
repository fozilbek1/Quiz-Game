print("Welcome to my computer quiz!")

play = input("Do you want to play? ")
if play != "yes":
    quit()
print("Okay! Let's play :)")
score = 0


answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct! ')
    score += 1
else: print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print('Correct! ')
    score += 1
else: print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct! ')
    score += 1
else: print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('Correct! ')
    score += 1
else: print("Incorrect!")

print ("You got " + str(score) + " question correct!")
print("You got " + str((score / 4) * 100) + "%.")

