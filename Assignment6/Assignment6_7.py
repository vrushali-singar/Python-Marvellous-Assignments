#accept 5 numberd from user and print max number
def max5(v1,v2,v3,v4,v5):
    max1 = v1
    if v2 > max1:
        max1 = v2
    if v3 > max1:
        max1 = v3
    if v4 > max1:
        max1 = v4
    if v5 > max1:
        max1 = v5
    print("max number :",max1)
def main():
    n1 = int(input("enter no1 :"))
    n2 = int(input("enter no2 :"))
    n3 = int(input("enter no3 :"))
    n4 = int(input("enter no4 :"))
    n5 = int(input("enter no5 :"))
    max5(n1,n2,n3,n4,n5)
if __name__ == "__main__":
    main()
    