num1= int(input("Enter a number: "))
num2= int(input("Enter another number: "))

if num2 == 0:
    print("Error: Divisor cannot be zero.")
else:
    quotient = num1 // num2
    print(f"The quotient of the 2 numbers is {quotient}.")