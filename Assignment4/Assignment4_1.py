#Write a program which contains one lambda function which accepts one parameter and return power of two.
power2 = lambda no : (no ** 2)
n = int(input("enter number :"))
ans = power2(n)
print("Answer is :",ans)