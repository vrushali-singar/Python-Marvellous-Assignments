#Accept a list of numbers and use filter() to keep only even numbers
def filterfunction(L):
    filteredList = list(filter(lambda x: x % 2 == 0 ,L))
    return filteredList


def main():
    n = int(input("Enter Number of elements :"))
    L1 = []
    print("enter values :")

    for i in range(n):
        no = int(input())
        L1.append(no)
    print("Elements are :")
    print(L1)
    ans = filterfunction(L1)
    print("even number are :",ans)


if __name__ == "__main__":
    main()