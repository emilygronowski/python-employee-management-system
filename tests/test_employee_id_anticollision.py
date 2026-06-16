from pytest import MonkeyPatch
from scripts.employee import Employee
from scripts.employee_id_anticollision import (
    adding_employee,
    find_available_id
)


class TestEmployeeIdAnticollision:
    def test_find_available_id_should_be_correct_before_insertion(
            self: TestEmployeeIdAnticollision
            ) -> None:
        id = find_available_id()
        assert id == 4

    def test_adding_employee_should_add_employee_with_proper_id(
            self: TestEmployeeIdAnticollision,
            monkeypatch: MonkeyPatch
            ) -> None:
        mock_employees = {
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            2: Employee("Mark Jones", "IT", "Programmer"),
            3: Employee("Joy Rogers", "Manufacturing", "Engineer")
        }

        monkeypatch.setattr(
            "scripts.employee_id_anticollision.employees",
            mock_employees
            )

        assert len(mock_employees) == 3
        assert 4 not in mock_employees

        adding_employee()

        assert len(mock_employees) == 4
        assert 4 in mock_employees
        assert mock_employees[4].name == "Sandy Smith"
        assert mock_employees[4].department == "AR"
        assert mock_employees[4].job_title == "Reimbursement Specialist"

    def test_find_available_id_should_return_proper_id_to_reuse(
            self: TestEmployeeIdAnticollision,
            monkeypatch: MonkeyPatch
            ) -> None:
        mock_employees = {
            4: Employee("Joy Rogers", "Manufacturing", "Engineer"),
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            3: Employee("Mark Jones", "IT", "Programmer")
        }

        monkeypatch.setattr(
            "scripts.employee_id_anticollision.employees",
            mock_employees
            )

        id = find_available_id()
        assert id == 2
