class Employee:
    # This is a class variable that keeps track of the ID count globally
    _id_counter = 1

    def __init__(self, name, department, job_title):
        # Assign the current counter value to the instance's id
        self.id = Employee._id_counter
        # Increment the global counter for the next employee
        Employee._id_counter += 1
        
        self.name = name
        self.department = department
        self.job_title = job_title

    # Replaces display_employee()
    def __str__(self):
        return f"Name: {self.name}\nDepartment: {self.department}\nJob Title: {self.job_title}\n"