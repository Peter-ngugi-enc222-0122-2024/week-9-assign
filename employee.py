class Employee:
    # Parameterized constructor
    def __init__(self, name, age, serviceyear, salary):
        self.name = name
        self.age = age
        self.serviceyear = serviceyear
        self.salary = salary

    # Destructor
    def __del__(self):
        print("Employee object destroyed")

    # Accessor (getter) methods
    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def getserviceyear(self):
        return self.serviceyear

    def getsalary(self):
        return self.salary


# Create an Employee object
emp = Employee("Frank Kibet", 30, 5, 75000)

# Access data using accessor methods
print("Name:", emp.getname())
print("Age:", emp.getage())
print("Service Year:", emp.getserviceyear())
print("Salary:", emp.getsalary())
