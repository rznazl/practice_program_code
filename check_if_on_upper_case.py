example_string = input("Enter any statement: ")

is_all_caps = True
found_letter = False

for char in example_string:
    if 'a' <= char <= 'z':
        is_all_caps = False
        break