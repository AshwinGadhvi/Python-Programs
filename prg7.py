cgos=int(input("Enter price of thing you byuy : "))
rev=int(input("Enter price of thing that you will sale : "))
oc=int(input("enter price of operating cost : "))


gs=rev-cgos
print("gross profit is : ",gs)

np=gs-oc
print("net profit is : ",np)

ans = np/(rev*100)
print("net profit in percentage is : ",ans)

