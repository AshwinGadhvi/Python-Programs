i=int(input("Enter number : "))
for i in range(1,41,3):
    if i%2==0:
        print(-i,end="")
    else:
        print(i)