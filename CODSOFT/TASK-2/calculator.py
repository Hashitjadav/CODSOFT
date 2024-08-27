def calculator():
    print(">>>>>>>>>  Calculator   <<<<<<<<<")
    Num_first = int(input("Enter first dight = "))
    Num_second = int(input("Enter second dight = "))

    print("Enter 1 for Addition \nEnter 2 for Subtraction \nEnter 3 for multiplication \nEnter 4 for Division")
    choice= int(input("Enter your choice: "))

    if choice == 1:
        print("Sum is ", int(Num_first + Num_second))
    elif choice == 2:
        print("Sub is ", int(Num_first - Num_second))
    elif choice == 3:
        print("Multiple is ", int(Num_first * Num_second))
    elif choice == 4:    
        print("Division is ", (Num_first / Num_second))
    else:
        print("Invalid choice")

    play_again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if play_again == 'yes':
        calculator()
    else:
        print("Thanks for using the calculator")
    
calculator()
            
