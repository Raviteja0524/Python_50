# coding Statement:  Write a program to find Sum of digits of a number

# Description

# Get a number from user and then find the sum of the digits in the given number.

# E.g. let the number = 341

# Sum of digits is 3+4+1= 8

# Input :4521

# Output :12

n=int(input("Enter your number : "))
num=str(n)
sum=0
for i in num:
    sum=sum+int(i)
print("sum :",sum)