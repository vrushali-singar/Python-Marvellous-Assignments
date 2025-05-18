#Write a program which accept number from user and return number of digits in that number.
def countDigits(n):
    count = 0
    if n == 0:
        return 1
    while n != 0:
        n = n // 10
        count = count + 1
    return count
    
       

def main():
    no = int(input("enter number :"))
    ans = countDigits(no)
    print("Number  of digits are :",ans)

  
    
if __name__ == "__main__":
    main()
