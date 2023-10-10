# coding Statement:  Write a program to identify if the number is even or odd

# Get a number as input from the user and check whether the given number is odd or even

# Input : 10

# Output : Even

# Input : 5

# Output : Odd


n=int(input())
if n==0:
    print("Nither Even Nor Odd")
elif(n%2)==0:
    print("Even")
elif(n%2)!=0:
    print("Odd")
