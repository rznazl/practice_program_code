numbers []

while True:
    user_input = input("Enter a number. Enter any letter to stop the program.")

    try:
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. The program will now stop.")
        break
