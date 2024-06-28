a=int(input("Enter sides a : "))
b=int(input("Enter sides b : "))
c=int(input("Enter sides c : "))

if (a+b)>c and (b+c)>a and (a+c)>b:
    print("b is form a triangle : ")
else:
    print("b is not form a triangl : ")