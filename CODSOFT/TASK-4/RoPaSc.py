import random
def play_game():
    item_list = ["rock", "paper", "scissors"]
    
    while True:
        user_input = input("Enter your choice - rock, paper, scissors: ").lower()
        
        if user_input in item_list:
            break  
        print("Invalid choice. Please enter a valid choice - rock, paper, scissors.")
        
    comp_choice = random.choice(item_list)

    print(f"User chose: {user_input}")
    print(f"Computer chose: {comp_choice}")

    if user_input == comp_choice:
        print("Both are the same, it's a tie.")

    elif user_input == "rock":
        if comp_choice == "paper":
            print("Paper covers rock, computer wins.")
        else:
            print("Rock crushes scissors, you win.")

    elif user_input == "paper":
        if comp_choice == "scissors":
            print("Scissors cut paper, computer wins.")
        else:
            print("Paper covers rock, you win.")

    elif user_input == "scissors":
        if comp_choice == "rock":
            print("Rock smashes scissors, computer wins.")
        else:
            print("Scissors cut paper, you win.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()  
    else:
        print("Thanks for playing!")

play_game()
