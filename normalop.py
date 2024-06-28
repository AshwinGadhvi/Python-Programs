tp=(10,20,40,60,50)
li=list(tp)
print(li)
li.sort()
tp=tuple(li)
print(tp)

t6=4,5,6
print(t6)
a,b,c=t6
print(a+b+c)
t7=("11111111")
print(t7)

for i in tp:
    print(i)

for i in range(len(tp)):
    print(tp[i])


tp55=(55,22,33,11,55,44,44,)
liop=list(tp55)
li3=[]
li4=[]
for i in tp55:
    if i not in li3:
        li3.insert(i,i)
    else:
        li4.append(i)
print(li3)
print(li4)

for i in li3:
    print("index of ",i," at position ",tp55.index(i))


even_square=tuple([x*x for x in range(1,11) if x%2==0])
print(even_square)
t11=(10,10,10)
t12=(20,20,20)
even_square=tuple([t11[x]+t12[x] for x in range(len(t11))])
print(even_square)

t11=(10,20,30,40,50,60,70)
print(t11[-6:-3:2])


#web grabbing