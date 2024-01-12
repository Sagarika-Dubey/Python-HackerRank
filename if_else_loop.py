'''Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''

a=int(input())
if(a%2 != 0):
    print("Weird")
elif(a%2==0 and a>=2 and a<=5):
    print("Not Weird")
elif(a%2==0 and a>=6 and a<=20):
    print("Weird")
elif (a%2==0 and a>20 ):
    print("Not Weird")
else:
    print('')    
