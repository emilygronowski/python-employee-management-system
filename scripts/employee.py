class Employee:
    def __init__(self, id, name, department, job_title):
        self.id = id
        self.name = name
        self.department = department
        self.job_title = job_title

    def display_employee(self):
        print(f"Name: {self.name}\nDepartment: {self.department}\nJob Title: {self.job_title}\n")