# Coding Statement:  Write a program to find Factorial of a number

# Description

# Get a number from user for which you need to fin the factorial, then calculate the factorial and give it as the output.

# Input : 4

# Output : 24

n=int(input())
fact=1
for i in range(1,n+1):
    fact=i*fact
print(fact)