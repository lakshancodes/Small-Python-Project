print("Welcome to my computer quiz!")

playing = input("Would you like to play? (y/n): ")

if playing.lower() != "y":
    print("Maybe next time! Goodbye :)")
    quit()

print("Okay! Let's play :)\n")

score = 0

question1 = input("What does CPU stand for? ")
if question1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Central Processing Unit'.")

question2 = input("What does GPU stand for? ")
if question2.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Graphics Processing Unit'.")

question3 = input("What does RAM stand for? ")
if question3.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Random Access Memory'.")

question4 = input("What does PSU stand for? ")
if question4.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Power Supply Unit'.")

print("\nYou got " + str(score) + " out of 4 questions correct!")
print("Your score: " + str((score / 4) * 100) + "%")
