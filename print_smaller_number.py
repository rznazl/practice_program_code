num1= float(input("Give a number: "))
num2= float(input("Give a 2nd Number"))

if num1 < num2:
    print(f"The smaller number is {num1}.")
elif num2 < num1:
    print(f"The smaller number is {num2}.")
else:
    print("Both numbers are equal.")