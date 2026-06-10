from scripts.employee import Employee

def test_employee_creation():
    # We no longer pass an ID number in the arguments
    emp = Employee("Susan Meyers", "Accounting", "Vice President")
    
    # We assert that the system assigned an integer ID automatically
    assert isinstance(emp.id, int)
    assert emp.name == "Susan Meyers"
    assert emp.department == "Accounting"
    assert emp.job_title == "Vice President"

def test_employee_string_representation():
    emp = Employee("Mark Jones", "IT", "Programmer")
    
    expected_output = "Name: Mark Jones\nDepartment: IT\nJob Title: Programmer\n"
    
    # str(emp) automatically triggers our new __str__ method
    assert str(emp) == expected_output