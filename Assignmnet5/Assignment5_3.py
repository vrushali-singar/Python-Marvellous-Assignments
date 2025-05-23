#Voting Eligibility Checker
#Accept age from the user and check whether the person is eligible to vote. (Age should be 18 or above.)
def Eligibility(value):
    if value <= 0:
        return "Enter valid age"
    elif value >= 18:
        return "Eligible to vote"
    else:
        return "Not Eligible to vote"
def main():
    n = int(input("Enter age :"))
    ans = Eligibility(n)
    print(ans)
if __name__ == "__main__":
    main()