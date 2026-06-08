# TESTER FOR EMPLOYEE MANAGER

import pytest
from employee_manager import employees, add_employee, get_employee, edit_employee, delete_employee

#clears the dictionary before every test run
@pytest.fixture(autouse=True)

def clear_employees():
    employees.clear()

def test_add_employee():
    add_employee(1, "Obi-Wan Kenobi", "Jedi", "Master")
    assert len(employees) == 1
    assert employees[1]["name"] == "Obi-Wan Kenobi"

def test_get_employee():
    add_employee(1, "Ash Ketchum", "Pokemon", "Trainer")
    emp = get_employee(1)
    assert emp["name"] == "Ash Ketchum"
    assert get_employee(99) is None  #quick test for id that doesn't exist

def test_edit_employee():
    add_employee(1, "Monkey Luffy", "Pirate", "Captain")
    success = edit_employee(1, name="John Doe")
    assert success is True
    assert employees[1]["name"] == "John Doe"

def test_delete_employee():
    add_employee(1, "Michael Scott", "Management", "Boss")
    success = delete_employee(1)
    assert success is True
    assert 1 not in employees
    assert delete_employee(99) is False # quick test for deleting an ID that wasn't inputted