#Write a program which accept one number from user and return its factorial.

def fact(n):
    result = 1 #Start with 1 because multiplying by 0 gives 0 
    for i in range(1,n+1):
        result = result * i
    return result

def main():
    no = int(input("enter number : "))
    if no < 0:
        print("For Negative number factorial can not be calculated ")
    else:
        ans = fact(no)
        print("Factorial is : ",ans)
    fact(no)
if __name__ == "__main__":
    main()