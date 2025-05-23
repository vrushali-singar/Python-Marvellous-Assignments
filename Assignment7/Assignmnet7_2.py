#Accept a list of integers from the user and use the map() function to double each value.
def Mapfunction(l):
    mapList = list(map(lambda x: x * 2 ,l))
    return mapList
    
def main():
    #create list
    n = int(input("enter number of elements :"))
    l1 = []
    print("enter value:")
    for i in range(n):
        no = int(input())
        l1.append(no)
    print("Entred values are:")
    print(l1)
    newList = Mapfunction(l1) #paasing the list
    print("Doubled values in list are:",newList)
    
if __name__ == "__main__":
    main()