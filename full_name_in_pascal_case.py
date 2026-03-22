full_name = input("Enter your full name in an incorrect casing (e.g., ReXi DiMaRaNaN): ")

pascal_case = full_name.title().replace(" ", "")
print("Full name in pascal case:", pascal_case)