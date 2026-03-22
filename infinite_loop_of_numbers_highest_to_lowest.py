numbers = []

print("Enter any number. Enter any letter to stop the program.")

while True:
    user_input = input("Enter here: ")
    try:
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        break
        
numbers.sort(reverse = True)

print("\nNumbers from highest to lowest: ")
print(numbers)