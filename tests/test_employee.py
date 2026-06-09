from scripts.employee import Employee

def test_employee_creation():
    # Create the object
    emp = Employee(47899, "Susan Meyers", "Accounting", "Vice President")
    
    # Assert the attributes were set correctly
    assert emp.id == 47899
    assert emp.name == "Susan Meyers"
    assert emp.department == "Accounting"
    assert emp.job_title == "Vice President"

def test_display_employee(capsys):
    # Test that the display method prints the exact requested string
    emp = Employee(47899, "Susan Meyers", "Accounting", "Vice President")
    emp.display_employee()
    
    captured = capsys.readouterr()
    expected_output = "Name: Susan Meyers\nDepartment: Accounting\nJob Title: Vice President\n\n"
    assert captured.out == expected_output