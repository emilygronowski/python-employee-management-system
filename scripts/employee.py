class Employee:
    def __init__(
            self: Employee,
            name: str,
            department: str,
            job_title: str
            ) -> None:
        self.name = name
        self.department = department
        self.job_title = job_title

    def __str__(self: Employee) -> str:
        return (
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Job Title: {self.job_title}"
        )
