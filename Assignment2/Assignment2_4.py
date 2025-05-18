#Write a program which accept one number form user and return addition of its factors.
def factordAddition(n):
    sum = 0
    for i in range(1, n):  # Factors are numbers less than 'n' that divide it completely
        if n % i == 0:
            sum += i
    return sum


def main():
    no = int(input("Enter number :"))
    ans = factordAddition(no)
    print("Addition of factors of number is  :",ans)
if __name__ == "__main__":
    main()
