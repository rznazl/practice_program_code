example_string = input("Enter any text: ")

if example_string:
    first_part = example_string[0].upper()
    rest_of_part = example_string[1:].lower()

    result = first_part + rest_of_part
else:
    result = ""

print("Output:", result)