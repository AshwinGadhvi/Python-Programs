n=int(input("how many number do you want to enter : "))
sum1=0
avg=0
for i in range(1,n+1):
    i=int(input("enter number:"))
    sum1+=i
    avg=sum1/n
print(sum1)
print(avg)