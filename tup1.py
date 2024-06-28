first_name=('ashwin','vishwaraj','jayraj','sidhu')
last_name=('gadhvi','jadeja','jadeja','sindhi')
ages=(18,21,20,19)
zipped=zip(first_name,last_name,ages)
print(zipped)
customers=tuple(zipped)
ashwin=customers[0]
print(ashwin)

first_name,last_name,ages=customers[2]
print(first_name,last_name,',',ages,'year old')

import sys
a_list=['abc','xyz',123,321,12.12,0.1221]
a_tuple=('abc','xyz',123,321,12.12,0.1221)
print('the list size is : ',sys.getsizeof(a_list),'bytes')
print('the tuple size is : ',sys.getsizeof(a_tuple),'bytes')

x=20
y=10
print('before swaping : ')
print(f'x={x},y={y}')
(x,y)=(y,x)
print('after swaping : ')
print(f'x={x},y={y}') 

x=(10,20)
y=x*2
print(y)
a=([1,2],['x','y'])
a[0][0]=99
a[1][0]='t'
print(a)

a=(3,0,2)
#a.sort error dega
#tuple object has no attribute 'sort'

a=(3,5,8,2)
b=sorted(a)
print(b)
print(type(b))

def count_sum(arr):
    count=len(arr)
    sum1 =sum(arr)
    return count,sum1

t=count_sum([10,20,30])
print(t)

#pip install numpy

import numpy as np
arr = np.random.randint(10,size=8)
a=count_sum(arr)
print(a)
(8,39)
print(type(a))
#del a use for delete element
#show numpy on details