#Accept a list of numbers and use reduce() (from functools) to find the product of all numbers.
from functools import reduce
def reduceFunction(L):
    ret = reduce(lambda x,y: x * y,L)
    return ret

def main():
    n = int(input("enter number of elements: "))
    L1 = []
    print("enter number:")
    for i in range(n):
        no = int(input())
        L1.append(no)
    print("Elements are :")
    print(L1)
    NewList = reduceFunction(L1)
    print("Product : ", NewList)

if __name__ == "__main__":
    main()