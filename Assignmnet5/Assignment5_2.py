#Vowel or Consonant Check
#Accept a single character from the user and check if it is a vowel (a, e, i, o, u). 
# If not, print it's a consonant.
def checkVowel(value):
    if len(value) != 1 or not value.isalpha():
        return "Invalid input. Please enter a single alphabet letter."
    if value == "a" or value == "e" or value == "i" or value == "o" or value == "u" :
        return f"{value} is vowel"
    else:
        return f"{value} is consonant" 
 #value.isalpha() checks alphabet letter (a to z or A to Z)
 #True for "a", "Z" False for "1", "@", " "
 #not reverses the result. So it becomes True when the input is not a letter.

def checkVowel2(w):
    if len(w) != 1 or not w.isalpha():
        return "Invalid input. Please enter a single alphabet letter."
    vowels = "aeiou"
    for i in vowels:
        if w == i:
            return f"{w} is vowel"

    f"{w} is consonant"

def main():
    char = input("enter a single letter :")
    ans = checkVowel(char)
    print(ans)
    ans2 = checkVowel2(char)
    print("ans using for loop :",ans2)

if __name__ == "__main__":
    main()
