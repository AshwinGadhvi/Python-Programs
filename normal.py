i=2
n=int(input("Enter the number to ind the prime or not  :"))
for i in range (n):
    if(n%i==0):
            flag=1
    else:
            flag=0
            break
if(flag==0):
    print("number is prime : ")
else:
    print("number is not prime : ")
