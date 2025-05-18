#1. Create on module named as Arithmetic which contains 4 functions 
# as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. 
# All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import arithmatic #icluding module arithmatic.py file

print("enter no1 :")
no1 = int(input())

print("enter no2 :")
no2= int(input())

addition = arithmatic.add(no1,no2)
print("Addition  is :",addition)

mutiplication = arithmatic.mult(no1,no2)
print("Multiplication  is :",mutiplication)

subtraction = arithmatic.sub(no1,no2)
print("Subtraction  is :",subtraction)

division = arithmatic.div(no1,no2)
print("Division  is :",division)


