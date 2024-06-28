number=int(input("Enter Number : "))
ans=number*9
l_digit=0
summ=0
while ans>0:
    l_digit=int(ans%10)
    summ=int(summ+l_digit)
    ans=int(ans/10)
print("Guess the animal from the last char of ans : ")
print("The Animal is elephant and number is 9")
