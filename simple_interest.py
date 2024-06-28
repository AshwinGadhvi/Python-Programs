#Practical 2 A

print("Performing Practical 2 A")
#created
lst=[1,2,3,4,5]
print("Created List Is  : ")
print(lst)

#append
print("Before Append : ")
print(lst)
lst.append(6)
print("After Append : ")
print(lst)

#extend
print("Before Extend : ")
print(lst)
lst2=[8,9,10,11]
lst.extend(lst)
print("After Extend : ")
print(lst)

#remove
print("BEfore Remove : ")
print(lst)
lst.remove(1)
print("After Remove : ")
print(lst)

#reverse
print("Before Reverse : ")
print(lst)

lst3=lst[::-1]
print("After Reverse : ")
print(lst3)

#ascending 
print("Printing List in ascending ")
lst3.sort()
print(lst3)

#descending 
print("Printing List in descending ")
lst3.sort(reverse=True)
print(lst3)

#Practical 2 B

print("Performing Practical 2 B")
print("Creating New List : ")
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana",
"orange"]]
print(List1)

#finding

print("Finding Python & banana from list : ")
print(List1[4][0],List1[8][2])

#Printing list
print(List1*5)

