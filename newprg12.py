p=int(input("Enter p : "))
r=int(input("Enter r : "))
n=int(input("Enter n : "))
emi=(p*r*(1+r)**n)/((1+r)**(n-1))
print(emi)