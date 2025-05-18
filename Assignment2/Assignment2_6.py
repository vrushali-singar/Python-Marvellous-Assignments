# print following pattern
# * * * * *
# * * * *
# * * * 
# * * 
# * 
def pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end =" ")
        print()

def main():
    no = int(input("enter number :"))
    pattern(no)

  
    
if __name__ == "__main__":
    main()
