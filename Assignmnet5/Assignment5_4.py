#Find Largest Among Three Numbers 
# Accept three numbers from the user and print the largest using nested if-else statements.
def largeNumber(v1,v2,v3):
    if v1 > v2 and v1 > v3:
        return v1
    elif v2 > v1 and v2 > v3:
        return v2
    else:
        return v3

def main():
    n1 = int(input("Enter first Number :"))
    n2 = int(input("Enter second Number :"))
    n3 = int(input("Enter third Number :"))
    ans = largeNumber(n1,n2,n3)
    print("largest Number is :",ans)
    
if __name__ == "__main__":
    main()