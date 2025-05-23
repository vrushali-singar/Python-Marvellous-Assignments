#print triangle pattern using nested loop
def pattern(no):
    for i in range(1,no+1):
        for j in range(i):
            print("*", end=" ")  
        print()
def pattern2(no):
    i = 1
    while i <= no:
        j = 1
        while j <= i:
            print("*", end = " ")
            j = j + 1
        print()
        i = i + 1
def main():
    n = int(input("Enter a number :"))
    print("using nested for loop")
    pattern(n)
    print("using nested while loop")
    pattern2(n)

if __name__ == "__main__":
    main()