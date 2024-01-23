while True:
    username = input ("Please enter your name: ")

    while True:
            num = int(input("Enter a positive integer between 1 and 100 inclusive: "))
            if 1 <= num <= 100:
                break
            else:
                print("Invalid input. Please enter a positive integer between 1 and 100.")

    if num % 2 == 1 and num < 60:
        print(f"Hello {username}! {num} is Odd and less than 60.")
    elif num % 2 == 0 and 2 <= num <= 24:
        print(f"Hello {username}! Even and less than 25.")
    elif num % 2 == 0 and 26 <= num <= 60:
        print(f"Hello {username}! Even and between 26 and 60 inclusive.")
    elif num % 2 == 0 and num > 60:
        print(f"Hello {username}! {num} is Even and greater than 60.")
    elif num % 2 == 1 and num > 60:
        print(f" Hello {username}! {num} is Odd and greater than 60.")


    stop_program = input("Do you want to stop? (yes/no): ").lower()
    if stop_program == 'yes':
        print("Goodbye!")
        break
