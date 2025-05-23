# Even or Odd Number Check
#Write a program to check whether the entered number is even or odd.
def checkEvenOdd(value):
    if value < 0:
        return "enter positive number"
    if value == 0:
        return "0 is neither odd nor even"
    elif value % 2 == 0:
        return "Given number is even"
    else:
        return "Given number is odd"

def main():
    n = int(input("enter number :"))
    ans = checkEvenOdd(n)
    print(ans)
if __name__ == "__main__":
    main()