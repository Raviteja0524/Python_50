#Get an input number from the user and check whether it is a positive or negative number.

#Input :-10

#Output : Negative number

#Input :0

#Output :Neither positive nor negative

#Input :15

#Output : Positive number




Num=int(input())
if Num>0:
    print('Positive Number')
elif Num<0:
    print('Negative Number')
else:
    print('Nither positive nor Negative')