#Arithmetic Operations on Two Numbers
#Write a program to accept two integers from the user and display their:
#Sum ,Difference ,Product ,Division
def addition2(value1,value2):
    result = value1 + value2
    return result 
def diffrence2(value1,value2):
    result = value1 - value2
    return result
def product2(value1,value2):
    result = value1 * value2
    return result
def division(value1,value2):
    if value2 != 0:  
        result = value1 / value2
        return result
    else:
        return "Cannot divide by zero"
def main():
    n1 = int(input("enter first number :"))
    n2 = int(input("enter second number :"))

    sum = addition2(n1,n2)
    print("Sum :",sum)

    Difference = diffrence2(n1,n2)
    print("Difference :",Difference)

    Product = product2(n1,n2)
    print("Product :",Product)

    Division = division(n1,n2)
    print("Division :",Division)

if __name__ == "__main__":
    main()








