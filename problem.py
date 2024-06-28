import math
from re import X
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))

delta = (math.pow(b,2))-(4*a*c)
x=math.pow(b,2)
if (delta==0):
    alpha=-(b/(2*a))
    beta=(b/(2*a))
    print(alpha)
    print(beta)
    print(delta)
elif(delta>0):
    alpha=(-b+math.sqrt(x-4*a*c))/2*a
    beta=(-b-math.sqrt(x-4*a*c))/2*a
    print(alpha)
    print(beta)
    print(delta)
    
else:
    print("roots are imagenary")