class A:
    a=10
    b=5
    c=0
    def __init__(self):
        self.c=self.a+self.b
        self.name="Ashwin"
        print(self.c,self.name)
    # def display(self):
    #     print(self.a+self.b)

class B(A):
    d=A.a
    def display2(self):
        print(self.d)

b=B()
b.display2()