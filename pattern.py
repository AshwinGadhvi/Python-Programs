n=int(input("Enter Range : "))
for i in range(1,n):
    for j in range(65,65+i):
        a = chr(j)
        print(a,end=" ")
    print()

