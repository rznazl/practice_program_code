example_string = input("Enter any statement: ")

is_all_caps = True
found_letter = False

for char in example_string:
    if 'a' <= char <= 'z':
        is_all_caps = False
        break
    if 'A' <= char <= 'Z':
        found_letter = True

result = is_all_caps and found_letter

print("Output: ", result)