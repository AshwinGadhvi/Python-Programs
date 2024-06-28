try:
    a=int(input("Enter Number 1 : "))
    b=int(input("Enter Number 2 : "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Error generate")
else:
    print("by")