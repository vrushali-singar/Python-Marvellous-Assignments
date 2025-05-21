#Write a program which contains one lambda function which accepts two parameters 
# and return its multiplication.
multiply = lambda a, b: a * b

no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))

result = multiply(no1, no2)

print("Multiplication is:", result)
