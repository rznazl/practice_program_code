example_string = input("Enter any text: ")

result = "".join([c.upper() if c.islower() else c.lower() for c in example_string])

print("Output:", result)