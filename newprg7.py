n=int(input("Enter number : "))
n1 , n2 = 0,1
print("fibonacci series is : ",n1,n2,end=" ") #0 1
for i in range(2,n):
    n3=n1+n2 #2
    n1=n2 #2
    n2=n3 #2
    print(n3,end=" ")
    
    