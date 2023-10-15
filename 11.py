# Coding Statement:  Write a program to find Fibonacci series up to n

# Description

# Fibonacci series is a special series where nth term is the sum of previous two terms in the series. The series starts with 0 and 1 as the first and second term of the series respectively.

# Here you need to get the value for nth term from user and then print Fibonacci series containing n terms.

# Input :5

# Output :0,1,1,2,3


n=int(input())
list=[0,1]
for i in range(1,n-2):
    l=list[-1]+list[-2]
    list.append(l)

for i in list:
    print(i,end=",")
    