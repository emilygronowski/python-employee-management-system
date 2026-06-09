class Employee:
    _counter = 1

    def __init__(self, name, department, job_title):
        self.id = Employee._counter
        self.name = name
        self.department = department
        self.job_title = job_title
        Employee._counter += 1

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Job Title: {self.job_title}"
    )
