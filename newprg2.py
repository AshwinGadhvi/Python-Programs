items=int(input("Enter total numbers of item : "))
if items <= 10:
    ans=items*120
    print("Total amount is : ",ans)
elif items >= 10 and items <=99:
    ans=items*100
    print("Total amount is : ",ans)
else:
    print("total amount is : ",items*70)