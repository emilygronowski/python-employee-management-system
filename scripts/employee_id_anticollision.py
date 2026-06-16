from scripts.employee import Employee

employees = {
    1: Employee("Susan Meyers", "Accounting", "Vice President"),
    2: Employee("Mark Jones", "IT", "Programmer"),
    3: Employee("Joy Rogers", "Manufacturing", "Engineer")
}


def find_available_id() -> int:
    index = 1

    while index in employees:
        index += 1

    return index


def adding_employee() -> None:
    id = find_available_id()
    employees[id] = Employee("Sandy Smith", "AR", "Reimbursement Specialist")
