#Write a function that accepts a list of integers and returns a list of prime numbers using filter().
import checkPrime

def primefilter(L):
    filteredlList = list(filter(lambda x: checkPrime.ChkPrime(x),L))
    return filteredlList


def main():
    n = int(input("Enter Number of Elements :"))
    L1 = []
    print("Enter elements :")
    for i in range(n):
        no = int(input())
        L1.append(no)
    print("Elements in list are:")
    print(L1)
    ans = primefilter(L1)
    print("List of prime numbers:",ans)

if __name__ == "__main__":
    main()