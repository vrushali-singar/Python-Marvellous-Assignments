#Write a program which accept one number for user and check whether number is prime or not.
def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True


def main():
    no = int(input("enter number :"))
    if isPrime(no):
        print("Number is prime")
    else:
        print("Number is not prime")

    
if __name__ == "__main__":
    main()
