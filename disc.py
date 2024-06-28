d1=dict(id=1,Fname="ashwin",Lname="Gadhvi",age="18") #constructer
d2={
    "id":2,
    "fname":"kishan",
    "Lname":"GAdhvi",
    "age":55
}
#where it is use
l1=[{"id":2,
    "fname":"kishan",
    "Lname":"GAdhvi",
    "age":55,
    "marks":[10,20,30,40,50]
    },{
        "id":3,
    "fname":"kishan",
    "Lname":"GAdhvi",
    "age":55,
    "marks":[10,20,30,40,50]
    },{
        "id":4,
    "fname":"kishan",
    "Lname":"GAdhvi",
    "age":55,
    "marks":[10,20,30,40,50]
    }]
print(l1)
print(l1[0]["fname"],["marks"])
print(l1[1]["marks"])
l1[0]["fname"]="ashwin"
print(l1)

#i contains keys
#only get the key
for key in l1:
    print(key)
d2={
    "id":4,
    "fname":"kishan",
    "Lname":"GAdhvi",
    "age":55,
    "marks":[10,20,30,40,50]
}

for key in d2:
    print(d2[key])

print(d2.get("fname"))
print(d2.get("age"))

d4={}
d4["id"]=2
d4["fname"]="ashwin"
d4["marks"]=[20,30,40,50]
d4["marks"]=[10,20,30,40,50]
print(d4)

d5={}
d5["marks"]=d4["marks"]
print(d5)

d6={}
d5["marks"]=40,50,60
print(d6)

d7=d5.copy()
d5.clear()
print(d7)

print(d7.keys())
print(d7.items())

d7.pop("marks")
print(d7)

for i in d4.values():
    print(i)
for i in d4.keys():
    print(i)
for i in d4.items():
    print(i)

d4.update({"marks":[20,30,40,50]})
print(d4)