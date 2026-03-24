sample_string = "Object Oriented Programming"
given_prefix = "Obj"

prefix_length = len(given_prefix)

beginning_part = sample_string[:prefix_length]

if beginning_part == given_prefix:
    result = True
else:
    result = False

print(f"Starts with '{given_prefix}':", result)