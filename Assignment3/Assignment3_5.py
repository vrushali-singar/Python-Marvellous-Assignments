#Write a program which accept N numbers from user and store it into List. 
# Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number 
# to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().

import MarvellousNum

def ListPrime():
    numbers = []
    n = int(input("Enter how many numbers you want to enter: "))
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    prime_sum = 0
    for num in numbers:
        if MarvellousNum.ChkPrime(num):
            prime_sum += num

    return prime_sum

def main():
    result = ListPrime()
    print("Addition of all prime numbers is:", result)

if __name__ == "__main__":
    main()
