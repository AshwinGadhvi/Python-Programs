p=int(input("Enter p : "))
r=int(input("Enter r : "))
n=int(input("Enter n : "))

ans=(p*r*(1+r)**n)/((1+r)**n-1)

print("answer is : ",ans)