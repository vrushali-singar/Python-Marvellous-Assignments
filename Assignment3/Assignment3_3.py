#Write a program which accept N numbers from user and store it into List. 
# Return Minimum number from that List. withosut using min function
def find_min(n):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    # Initialize minimum with the first element
    minimum = numbers[0]

    # Traverse the list to find the minimum manually
    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum

def main():
    n = int(input("How many numbers do you want to enter? "))
    result = find_min(n)
    print("Minimum number is:", result)

if __name__ == "__main__":
    main()
