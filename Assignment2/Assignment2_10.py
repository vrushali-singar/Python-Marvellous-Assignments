#Write a program which accept number from user and return addition of digits in that number.
def addDigits(n):
    sum = 0
    while n != 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10 
    return sum  

def main():
    no = int(input("enter number :"))
    ans = addDigits(no)
    print("Addition  of digits are :",ans)

  
    
if __name__ == "__main__":
    main()
