class boss:
    def myboss(self):
        print("i am the boss")

class Employee(boss):
    employeeCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.employeeCount+=1

    def displaycount(self):
        print ("employeeCount is ",Employee.employeeCount)
        print(self.name)

em1=Employee("vishal",1000)
print(em1.myboss())



