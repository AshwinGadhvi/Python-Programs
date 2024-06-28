p=int(input("Enter p : "))
r=int(input("Enter r : "))
t=int(input("Enter t : "))
n=int(input("Enter n : "))
si=(p*r*t)/100
ci=p*(1+(r/100*n))**n*t

print("simple interst is : ",si)
print("Compuond interse is : ",ci)