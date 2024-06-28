a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))
sum1=0

sum1=a+b+c
print(sum1)
if(a==b==c):
    print("0")
elif(a==b):
    print(c)
elif(b==c):
    print(a)
elif(a==c):
    print(b)
else:
    print(sum1)




