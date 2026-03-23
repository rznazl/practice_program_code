sample_statement = "I love my life"

converted_statement = " ".join([word[0].upper() + word[1:].lower() for word in sample_statement.split()])

print(f"Original: {sample_statement}")
print(f"Result: {converted_statement}")