# a set contains unique elements
s1 = set([1, 2, 1, 3, 4])   
print(s1)   # it will remove the duplicate elements and print the set

s1.add(5)
print(s1)
s1.discard(5)
print(s1)

s2 = set(s1)
for i in s1:
    if i>2:
        # print(i)
        s2.discard(i)
s1 = s2
print(s1)

s1 = set([1, 2, 3, 4, 6])
s2 = set([1, 2, 4, 5, 7])
s3 = set([1, 2, 4, 5, 9])

#union          (di5splays data from both locations without any duplication)
print(s1 | s2)

#intersection   (displays data from both locations which are common)
print(s1 & s2 & s3)

#ex-or          (displays data from both locations which are not common)
print(s1^s2)

# difference of two sets
print(s1-s2)
print(s2-s1)

# intersection of three sets using intersection_update function
s3.intersection_update(s1, s2)
print(s3)

# difference using function
print(s1.difference(s2))

# difference of three set
print(s3.difference_update(s1, s2))

# check for subset
s1 = set([1, 2, 3])
s2 = set([3, 2, 4])
if(s1>s2):
    print("s2 is subset of s1")
else:
    print("s2 is not a subset of s1")

print(min(s1))
print(max(s1))
print(len(s1))

s3 = s1.copy()
print(s3)

# isdisjoint
s1 = set([1, 5, 6])
s2 = set([3, 2, 4])
print(s2.isdisjoint(s1))

# pop
print(s3)
s3.pop()
print(s3)