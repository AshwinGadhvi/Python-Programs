print("What do you want to find ?")
print("1.For Area of circle : ")
print("2.For Area of Perimeter : ")
n=int(input("Enter your choice : "))

if n == 1:
    r=int(input("Enter redius : "))
    print("Area of redius is : ",3.14*r*r)
elif n == 2:
    r=int(input("Enter redisu : "))
    print("Perimeter of circle : ",2*3.14*r)
else:
    print("Enter Valid choice : ")
    