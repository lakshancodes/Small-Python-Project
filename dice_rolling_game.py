import random

while True:
    user_input = input("Roll the dice? (y/n): ").lower()
    if user_input == "y":
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        print(f"({roll1},{roll2})")
    elif user_input == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice! Please try again.")