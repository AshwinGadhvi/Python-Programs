import os
def pelindrome(z):
    z1=z[::-1]
    if z==z1 and len(z)>1:
        return z
    else:
        return ''

frame = input("Enter File Name : ")


if not os.path.exists(frame):
    print("invalid file name")
else:   
    f = open(frame)
    data = f.read(100)
    print(data)
    # data=f.readline()
    # print(data.split(","))
    # data=f.readline(10)
    # print(data)
    # data =f.readlines()
    # print(len(data))
    data = f.read()
    r=data.split(" ")
    # print(len(r))
    
    for w in r:
        t=pelindrome(w)
        if t != '':
            print(t)
    f.close()

