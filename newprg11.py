li=[]

for i in range(0,10):
    li+=list(input())
print(li)
mini=li[0]
for i in li:
    if(mini>i):
        mini=i
print(mini)

mini2=li[0]
for i in li:
    if(mini<i and mini2>i):
        mini2=i
print(mini2)
        