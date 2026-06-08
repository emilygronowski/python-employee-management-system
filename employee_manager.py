#   Structure: {id: {"name": str, "department": str, "job_title": str}}

employees = {}

def add_employee(emp_id, name, department, job_title):
    #adds a new employee to the employees dictionary
    employees[emp_id] = {
        "name": name,
        "department": department,
        "job_title": job_title
    }

def get_employee(emp_id):
    #returns the employee details for the given employee ID
    return employees.get(emp_id)

def edit_employee(emp_id, name=None, department=None, job_title=None):
    #edits the employee details for the given employee ID
    if emp_id in employees:
        if name:
            employees[emp_id]["name"] = name
        if department:
            employees[emp_id]["department"] = department
        if job_title:
            employees[emp_id]["job_title"] = job_title
        return True
    return False

def delete_employee(emp_id):
    #deletes the employee from the employees dictionary
    if emp_id in employees:
        del employees[emp_id]
        return True
    return False  