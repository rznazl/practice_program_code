full_name = input("Enter your name in incorrect casing (e.g., AiZeLlE dElOs ReYeS): ")

snake_case = full_name.lower().replace(" ", "_")
print("Full name in snake_case:", snake_case)