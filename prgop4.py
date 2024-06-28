
li=[]
for i in range(12):
    li.insert(i,int(input("Enter number : ")))
print(li)
for i in range(len(li)):
    if(li[i]>10):
        li[i]=10
print(li)