# Print Sum of Even Numbers Between 1 and 100. 
# Use a loop to find and print the sum of all even numbers from 1 to 100.
#Expected Output:Sum of even numbers between 1 to 100 is: 2550
sum = 0
print("using for loop")
for i in range(1,101):
    if i % 2 == 0:
        sum = sum + i 
      
print("sum of all even numbers from 1 to 100 is ",sum)

print("----------------------------------")

print("using while loop")
total = 0
n = 1
while n <= 100:
    if n % 2 == 0:
        total = total + n
    n = n + 1
print(sum)
