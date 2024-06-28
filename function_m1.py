__functionCallCount=0

#function with no arguement
def myfunc():
    global __functionCallCount
    __functionCallCount+=1
    print("hellow")

#function with arguement
def summer(a,b):
    global __functionCallCount
    __functionCallCount+=1
    a1=a
    b1=b
    ans=a1+b1
    print(ans)

#function with arguement
def power(x,y):
    global __functionCallCount
    __functionCallCount+=1
    return x**y

#function with defualt arguement
def power(x,y=2):
    return x**y

def prime(x):
    flag=0
    for i in range(2,x):
        if x % i == 0:
            flag=1
            break
    if flag == 0:
        print("number is prime : ",x)
    else:
        print("number is not prime",x)

def fact(n):
    mul=1
    for i in range(1,n):
        mul+=(mul*i)
    print(mul)
def powerop(x,y):
    p=1
    if y==1:
        return x
    else:
        p=y*power(x,y-1)
    return p 
myfunc()
summer(10,20)
print("power pf 2 raise to 3 is ",power(2,3))
print("power of 2 raise to 2 is ",power(2))
prime(11)

def showFunctionCount():
    print("Funcation called : ",__functionCallCount)