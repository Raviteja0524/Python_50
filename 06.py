
# coding Statement:  Write a program to find the Quadrants in which coordinates lie

# Get the value of x and y coordinates as input from the user and check in which quadrant the point lies and print it.

# Input :10 20

# Output : This point lies in first quadrant.

# Input : -10 20

# Output : This point lies in second quadrant.


x,y=int(input()),int(input())
if x>0 and y>0:
    print("This point lies in first quadrant.")
elif   x<0 and y>0:
    print("This point lies in second quadrant.") 
elif   x<0 and y<0:
    print("This point lies in third quadrant.")
elif   x>0 and y<0:
    print("This point lies in fourth quadrant.")        
