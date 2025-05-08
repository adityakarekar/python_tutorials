from random import choice

while True:
    random_number = choice(range(1,4))

    computer_choice = ""
    if random_number == 1:
        computer_choice = "snake"
    elif random_number == 2:
        computer_choice = "water"
    elif random_number == 3:
        computer_choice = "gun"


    user_choice = input("Enter your choice (snake/water/gun): ").lower()
    print("User choice is: ", user_choice)
    if user_choice not in ["snake", "water", "gun"]:
        print("Invalid choice! Please choose either snake, water, or gun.")
        break
    print("Computer choice is: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
        continue
    elif (user_choice == "snake" and computer_choice == "water") or (user_choice == "water" and computer_choice == "gun") or (user_choice == "gun" and computer_choice == "snake"):
        print("You win!")
        break
    else:
        print("You lose!")
        break