class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_employee(self):
        print(f"Name: {self.name}, ID: {self.id_number}, Department: {self.department}, Job Title: {self.job_title}")

# Create the objects
emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
emp3 = Employee("Joy Rodgers", 81774, "Manufacturing", "Engineer")

# Display the data
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()