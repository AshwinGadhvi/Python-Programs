n=int(input("Enter number : "))
for i in range(1,n+1,3):
    if i % 2 == 0:
        print(-i,end=" ")
    else:
        print(i,end=" ")