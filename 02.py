#Take an input character from user and check whether it is an alphabet or not.

#Input :

#A

#Output: 

#Alphabet

#Input:

#7

#Output:

#Not an alphabet



c=str(input())
if ((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z')):
   print("Alphabet")
else:
    print("NOt an Alphabet")