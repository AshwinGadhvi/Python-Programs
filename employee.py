class Employee:
    #globally shared code with example
    e_name=""
    e_age=""

    def __init__(self,ename,eage):
        self.e_name=ename
        self.e_age=eage
    def show_employee(self):
        print("Name : ",self.e_name)
        print("age : ",self.e_age)
        