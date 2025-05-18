#Write a program which accept N numbers from user and store it into List. 
# Return addition of all elements from that List.
def listAddition(no):
    numbers = []
    for i in range(no):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    total = sum(numbers)
    return total

def main():
    n = int(input("How many numbers do you want to enter? "))
    result = listAddition(n)
    print("Addition of all elements is:", result)

if __name__ == "__main__":
    main()