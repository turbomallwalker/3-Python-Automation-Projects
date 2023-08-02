print("Hello User, welcome to my quiz!")

playing = input("Would you like to play a game? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's party!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('You got it!')
    score += 1
else:
    print("Bummer! Not correct. Try again!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('You got it!')
    score += 1
else:
    print("Bummer! Not correct. Try again!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('You got it!')
    score += 1
else:
    print("Bummer! Not correct. Try again!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('You got it!')
    score += 1
else:
    print("Bummer! Not correct. Try again!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100)+ "%.")

