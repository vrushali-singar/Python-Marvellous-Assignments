#Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that number from List.
def count_frequency(n, target):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Count how many times target appears in the list
    count = 0
    for num in numbers:
        if num == target:
            count += 1

    return count

def main():
    n = int(input("How many numbers do you want to enter? "))
    target = int(input("Enter the number to find frequency of: "))
    freq = count_frequency(n, target)
    print("The frequency is:",freq)

if __name__ == "__main__":
    main()
