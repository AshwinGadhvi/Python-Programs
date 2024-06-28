import math
a=int(input("Enter A : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

s=(a+b+c)/2
print(s)

area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)