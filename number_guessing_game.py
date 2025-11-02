import random

randnum = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number 1 - 100: "))
        if guess < randnum:
            print("Too Low")
        elif guess > randnum:
            print("Too High")
        else:
            print("Perfect! You got it!")
            break
    except ValueError:
        print("Invalid Guess! Try Again.")


