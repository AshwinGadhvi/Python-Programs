li=[10,20,30,40]
li2=[10,0,30,40]
flag=0
for i in range(len(li)):
    if(len(li)==len(li2)):
        if(li[i]==li2[i]):
            flag=1
        else:
            flag=0
            break
    else:
        flag=0
        break
if(flag==1):
    print("both are same")
else:
    print("both are diffrent")
