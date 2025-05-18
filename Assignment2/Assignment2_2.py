#Write a program which accept one number and display below pattern.
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
        print ()
def main():
    no =  int(input("enter number to print pattern:"))
    pattern(no)
    


if __name__ == "__main__":
    main()
