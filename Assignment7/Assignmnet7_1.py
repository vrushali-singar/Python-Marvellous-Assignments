#Write two lambda functions:
#One to calculate square of a number
#Another to calculate cube of a number

square = lambda x: x ** 2
cube = lambda n: n ** 3

def main():
    n = int(input("Enter numner :"))
    ans1 = square(n)
    ans2 = cube(n)
    print("square of number is:",ans1)
    print("cube of number is:",ans2)

if __name__ == "__main__":
    main()