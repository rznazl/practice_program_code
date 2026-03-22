full_name = input("Enter your full name with spaces in the beginning: ")

index = 0
while index < len(full_name) and full_name[index] == " ":
    index += 1

output = full_name[index:]

print("Output: ", output)