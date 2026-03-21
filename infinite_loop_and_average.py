numbers = []
while True:
    value = input("Enter any number. Enter any letter to stop: ")
    try:
        numbers.append(int(value))
    except ValueError:
        break

if numbers:
    average_of_all_numbers = sum(numbers) / len(numbers)
    print(f"The Average of all the numbers is {average_of_all_numbers}.")
else:
    print("No numbers were entered.")