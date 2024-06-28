n=int(input("Enter number : "))
l_digit=0
while n!=0:
    l_digit=n%100
    print(l_digit)
    n=int(n/100)


