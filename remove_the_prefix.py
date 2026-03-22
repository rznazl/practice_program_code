statement = "I love my life"
prefix = "I"

if statement.startswith(prefix):
    result = statement[len(prefix):]
else:
    result = statement

print("Statement without the prefix: ", result)