#Write a function that accepts a string and checks whether it is a palindrome.
def checkPalindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True
def main():
    char = input("enter string :")
    if checkPalindrome(char):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    

if __name__ == "__main__":
    main()