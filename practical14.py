# B.Tech Computer Science and Engineering(Software Engineering)
# Balkrishna Mehta
# 202103103510434
class employee:
    emp_name = None
    emp_age = None
    emp_city = None
    def get_data(self, name, age, city):
        self.emp_name = name
        self.emp_age =  age
        self.emp_city = city
class emp_derived(employee):
    def __init__(self, obj):
            print("Employee's Name:", obj.emp_name)
            print("Employee's Age:", obj.emp_age)
            print("Enployee's City:", obj.emp_city)

obj = employee()
obj.get_data(input("Enter Employee Name: "), input("Enter Employee's Age: "), input("Enter Employee's City: "))
print("----------------------------------------------")
emp_derived(obj)
