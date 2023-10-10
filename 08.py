# Coding Statement:  Write a program to find roots of a quadratic equation

# Description

# Get the values of a, b and c (coefficients of quadratic equation) as input from the user and calculate the roots and print as the output.

# Input : Enter the value of a, b and c : 1 -6 9

# Output : Roots are equal

# Root 1= root 2 = 3.00

import cmath
a=int(input("enter a value : "))
b=int(input("enter b value : "))
c=int(input("enter c value : "))
m=(b*b)-(4*a*c)
n=cmath.sqrt(m)
x1=(-b+n)/2*a
k=cmath.sqrt(m)
x2=(-b-n)/2*a
if m==0:
    print("roots are equal")
    print("root1=root2=",end="")
    print(x1.real or x2.real)
elif m>0:
    print("roots are different")
    print("root1=",x1.real ,"root2=",x2.real)
else:
    print("roots are complex")
    print("root1=",x1 ,"root2=",x2)