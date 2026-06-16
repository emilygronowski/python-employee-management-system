import pytest
from pytest import CaptureFixture

from app.models.employee import Employee


class TestEmployee:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys: CaptureFixture[str]) -> None:
        self.capsys = capsys

    def test_employee_instantiations(self) -> None:
        employee1 = Employee("Susan Meyers", "Marketing", "Vice President")
        employee2 = Employee("Mark Jones", "IT", "Programmer")
        employee3 = Employee("Joy Rodgers", "Manufactoring", "Engineer")

        print(employee1, employee2, employee3, sep="\n\n")
        captured = self.capsys.readouterr()
        assert captured.out == (
            "Name: Susan Meyers\n"
            "Department: Marketing\n"
            "Job Title: Vice President\n\n"
            "Name: Mark Jones\n"
            "Department: IT\n"
            "Job Title: Programmer\n\n"
            "Name: Joy Rodgers\n"
            "Department: Manufactoring\n"
            "Job Title: Engineer\n"
        )
