# Coding Statement : Write a program to reverse a given number

# Description

# Get an input from the user and the print the reverse of the given number as the output

# E.g. let the number be 324 then the reverse of the number is 423

# Input : 675

# Output : 576


n=int(input("enter your number : "))
x=0
while n!=0:
    y=n%10
    x=(x+y)*10
    n=n//10
print(x//10)
