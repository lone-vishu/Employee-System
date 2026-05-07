class Employee:
    def __init__(self,role, department, salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print(f"Role is: {self.role}")
        print(f"Department is: {self.department}")
        print(f"Salary is: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",45000)

e1=Employee('HR','Marketting',60000)
e1.showDetails()

e2=Engineer("Rahul",30)
e2.showDetails()
