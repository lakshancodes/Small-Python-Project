import random

choices = ["r", "p", "s"]
emojis = {"r": "🪨", "p": "📄", "s": "✂"}

def display_choices(user_choice, computer_choice):
        print(f"You chose {emojis[user_choice]}")
        print(f"Computer chose {emojis[computer_choice]}")

while True:

    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ")
    computer_choice = random.choice(choices)

    if user_choice.lower() not in choices:
        print("Invalid Choice! Please Try Again.")

    else:
        display_choices(user_choice, computer_choice)

        if user_choice == computer_choice:
            print("Tie!")

        elif ((user_choice == "r" and computer_choice == "s") or 
             (user_choice == "p" and computer_choice == "r") or 
             (user_choice == "s" and computer_choice == "p")):
            print("You win!")
            
        else:
            print("You lose.")
        
        should_continue = input("Contine? (y/n): ").lower()
        if should_continue == "n":
            break