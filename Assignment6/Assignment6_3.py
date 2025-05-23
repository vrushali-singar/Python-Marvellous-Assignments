#Accept a number from the user and print its multiplication table up to 10.
def multiplicationTable(n):
    for i in range(1,11):
        print(n, "*", i, "=", n * i)

def multiplicationTable2(v):
    i = 1
    while i <= 10:
        print(v , "*" , i , "=", v * i)
        i = i + 1
    print(i)

def main():
    no = int(input("Enter number :"))
    print("Multiplication(for loop) table is :")
    multiplicationTable(no)
    print("Multiplication(while loop) table is :")
    multiplicationTable2(no)

if __name__ == "__main__":
    main()
