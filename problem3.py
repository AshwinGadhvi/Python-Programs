n=int(input("Enter number : "))
for i in range(1,n):
    if i%2==0:
        print(i,"=",i)
    else:
        print(i,"=",i," (prime)")