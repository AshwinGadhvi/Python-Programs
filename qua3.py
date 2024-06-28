p=int(input("Enter p : "))
r=int(input("Enter r : "))
n=int(input("Enter n : "))
t=int(input("Enter t : "))
si=(p*r*n)/100
ci=p*(1+(r/n))**(n*t)
print(si)
print(ci)
ans=si+ci
print(ans)