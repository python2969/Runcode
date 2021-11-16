class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "."+last+"@gmail.com"

    def fullname(self):
        print ("{} {}".format(self.first, self.last))


emp_1 = Employee("Corpy","Lee", 5000)
emp_2 = Employee("Tony", "Kim", 600)

print(emp_1.email)
print (emp_1.fullname())
