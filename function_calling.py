import function_m1 as mp
import employee as e
import access_specifier as ac
#if __name__ == '__main__':
mp.prime(10)
mp.myfunc()
mp.summer(10,20)
mp.power(2,3)
mp.fact(5)
print(mp.powerop(2,3))

emp = e.Employee("ashwin","18")
emp.show_employee()


emp2 = ac.Employee("ashwin","18","50000","7046862268")
emp2.show_employee()

mp.showFunctionCount()