#Write a program which accept N numbers from user and store it into List.
#  Return Maximum number from that List.
def find_max(n):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    # Initialize maximum with the first element
    maximum = numbers[0]
    
    # Compare each number with current maximum
    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum

def main():
    n = int(input("How many numbers do you want to enter? "))
    result = find_max(n)
    print("Maximum number is:", result)

if __name__ == "__main__":
    main()
