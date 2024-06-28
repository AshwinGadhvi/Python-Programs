#string

Name = "Ashwin GAdhvi"
# treated as array
print(Name[1:6]) #[start,end]
print(Name)


ln=2
print(Name[ln])

#list
li=[0]
lst = [10,20,30,40]
lst[2]="ashwin"
print(lst[0:3])
lst[0:3]=["ashwin","gadhvi","master"]
print(lst)

lst[0]=[20,50,20]
print(lst)
print(lst[0][1])

lst[0][1]=[50,60,70]
print(lst)
print(lst[0][1][2])

#tuple

tpl=(10,20,30,40)
print(tpl[0:3])
tpl=(10,20,30,[10,20,30,40])
print(tpl[3][2])

#dictionary

dic={"206530307002":["Ashwin","computer","sem 4","Adipur","99999999999"],"206530307003":["hem","computer","sem 5","anjar","888888888888"]}
print(dic["206530307002"])
print(dic["206530307003"])

student = {"7001":{"Name":"sneh","Address":"Anjar","mobile":"9090909090"},"7002":{"Name":"vansh","Address":"bhuj","mobile":"9090909090"}}
print(student["7001"]["Name"])

lst=dic
print(lst)

str1="ashwin"
print(type(str1))

print(id(tpl))
#other then o is true other then one is false

#list function
new1 = list(("ashwin","bhargav","mukul"))
print(new1)

print(type(new1)) #return class type

li.append(new1) #append
print(li)

li = new1.copy() #copy
print(lst)

print(li.count("abc"))  #count
li.extend([10,20,30]) #insert
print(li)

print(li.index(20)) #show the value on first accurance
li.insert(2,"ashwin") #insert by potision
print(li)

print(li.pop(2)) #delete the element by index
print(li)


print(li.remove(10)) #delete by value
print(li)

li.reverse() #reverse
print(li)

# sort only integer or string if do reverse then write reverse=true

li2=[10,40,30,20,5,1,0]
li2.sort()
print(li2)

li3=["ashwin","mukul","bhargav","ansh"]
li3.sort()
print(li3)


a="ashwin"

if a in li3:
    print("Element found ")
else:
    print("Element not found ")

odd_square = [x**2 for x in range(1,11) if x%2 != 0]
print(odd_square)

print_table = [ 5*i for i in range(1,11)  ]
print(print_table)

# + oprator is used to merge two list


#spilt function

strop = "my name is ashwin"
l5=strop.split(" ")
print(l5)

l6 = list(strop)
print(l6)

k="n"

if k in l6:
    print("element found ",l6.index(k))
else:
    print("Element not found ")