class Employee:
    #globally shared code with example
    #private
    __e_name= None
    __e_age= None
    #protected
    _e_sal = None
    mob_no = None
    def __init__(self,ename,eage,esal,mob):
        self.__e_name=ename
        self.__e_age=eage
        self._e_sal=esal
        self.mob_no=mob
    def show_employee(self):
        print("Name : ",self.__e_name)
        print("age : ",self.__e_age)
        print("Salary : ",self._e_sal)
        print("Mobile : ",self.mob_no)
        