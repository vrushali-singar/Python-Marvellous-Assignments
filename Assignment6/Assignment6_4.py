#Accept a number and print its factorial using a for loop.
def Factorial(no):
    Fact = 1
    while (no >= 1):
        Fact = Fact * no
        no = no - 1
    return Fact

def Factorial2(no):
    sum = 1
    for i in range(1,no+1):
        sum = sum * i
    return sum

def main():
    n = int(input("Enter number :"))
    ans = Factorial(n)
    print("factorail is(using for while loop) :",ans)
    ans2 = Factorial2(n)
    print("factorail is(using for  loop) :",ans2)

if __name__ == "__main__":
    main()