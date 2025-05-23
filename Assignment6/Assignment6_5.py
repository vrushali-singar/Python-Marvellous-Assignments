#Accept a number from the user and check whether it is prime or not.
def primeNo(no):
    if no < 0 :
        return "enter positive number"
    if no == 0 :
        return "0 is nor prime nor composite"
    if no == 1 :
        return "1 is nor prime nor composite"
    if no == 2 :
        return "2 is  prime  number"
    count = 0
    i = 1
    while i <= no:
        if no % i == 0:
            count = count + 1
        i = i + 1
    if count == 2 :
        return "number is prime"
    else:
        return "number is not prime"

def main():
    n = int(input("Enter number :"))
    ans = primeNo(n)
    print(ans)
if __name__ == "__main__":
    main()