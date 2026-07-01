import builtins
import csv
from typing import Any
from unittest.mock import call, mock_open, patch

import pytest
from pytest import CaptureFixture, MonkeyPatch

from app.main import (
    add_employee,
    change_employee,
    find_available_id,
    load_employees,
    lookup_employee,
    main,
    save_employees,
)
from app.models.employee import Employee


class TestMain:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys: CaptureFixture[str]) -> None:
        self.capsys = capsys

    @pytest.fixture
    def mock_add_employee(self, monkeypatch: MonkeyPatch) -> Any:
        def mock_add_employee(employees: dict[int, Employee]):
            pass

        monkeypatch.setattr("app.main.add_employee", mock_add_employee)

    @pytest.fixture
    def mock_change_employee(self, monkeypatch: MonkeyPatch) -> Any:
        def mock_change_employee(employees: dict[int, Employee]):
            pass

        monkeypatch.setattr("app.main.change_employee", mock_change_employee)

    @pytest.fixture
    def mock_csv_data(self, monkeypatch: MonkeyPatch) -> None:
        mock_data = [
            ["1", "Susan Meyers", "Accounting", "Vice President"],
            ["2", "Mark Jones", "IT", "Programmer"],
            ["3", "Joy Rogers", "Manufacturing", "Engineer"],
        ]

        def mock_csv_reader(data: Any):
            return mock_data

        monkeypatch.setattr(csv, "reader", mock_csv_reader)

    @pytest.fixture
    def mock_load_employees(self, monkeypatch: MonkeyPatch) -> dict[int, Employee]:
        mock_employees: dict[int, Employee] = {}

        def mock_load_employees():
            return mock_employees

        monkeypatch.setattr("app.main.load_employees", mock_load_employees)

        return mock_employees

    @pytest.fixture
    def mock_lookup_employee(self, monkeypatch: MonkeyPatch) -> Any:
        def mock_lookup_employee(employees: dict[int, Employee]):
            pass

        monkeypatch.setattr("app.main.lookup_employee", mock_lookup_employee)

    @pytest.fixture
    def mock_open_file(self, monkeypatch: MonkeyPatch) -> Any:
        mock_open_file = mock_open()
        monkeypatch.setattr(builtins, "open", mock_open_file)
        return mock_open_file

    @pytest.fixture
    def mock_save_employees(self, monkeypatch: MonkeyPatch) -> Any:
        def mock_save_employees(employees: dict[int, Employee]):
            pass

        monkeypatch.setattr("app.main.save_employees", mock_save_employees)

    def test_load_employees_should_return_empty_dictionary(
        self,
        mock_open_file: Any,
    ) -> None:
        employees = load_employees()
        assert not employees

    def test_load_employees_should_raise_filenotfounderror_and_return_empty_dictionary(
        self,
    ) -> None:
        with patch("builtins.open", side_effect=FileNotFoundError):
            employees = load_employees()
            assert not employees

    def test_load_employees_should_add_csv_data_entries_to_dictionary(
        self, mock_csv_data: Any, mock_open_file: Any, monkeypatch: MonkeyPatch
    ) -> None:
        employees = load_employees()

        assert len(employees) == 3
        assert str(employees[1]) == (
            "Name: Susan Meyers\nDepartment: Accounting\nJob Title: Vice President"
        )
        assert str(employees[2]) == (
            "Name: Mark Jones\nDepartment: IT\nJob Title: Programmer"
        )
        assert str(employees[3]) == (
            "Name: Joy Rogers\nDepartment: Manufacturing\nJob Title: Engineer"
        )

    def test_save_employees_should_write_employees_to_file(
        self, mock_open_file: Any
    ) -> None:
        mock_employees: dict[int, Employee] = {
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            2: Employee("Mark Jones", "IT", "Programmer"),
            3: Employee("Joy Rogers", "Manufacturing", "Engineer"),
        }

        save_employees(mock_employees)

        mock_open_file.assert_called_once_with("employees.csv", "w")
        assert mock_open_file().write.call_count == 3

        expected_calls = [
            call("1,Susan Meyers,Accounting,Vice President\n"),
            call("2,Mark Jones,IT,Programmer\n"),
            call("3,Joy Rogers,Manufacturing,Engineer\n"),
        ]

        mock_open_file().write.assert_has_calls(expected_calls, any_order=False)

    def test_lookup_employee_should_display_error_if_no_employees_exist(self) -> None:
        lookup_employee({})
        captured = self.capsys.readouterr()
        assert captured.out.count("ERROR: No employees exist.") == 1

    def test_lookup_employee_should_raise_error_when_employee_does_not_exist(
        self, monkeypatch: MonkeyPatch
    ) -> None:
        def mock_input(prompt: str) -> str:
            assert prompt == "Enter an employee ID: "
            return "1"

        monkeypatch.setattr("builtins.input", mock_input)

        mock_employees: dict[int, Employee] = {
            2: Employee("Susan Meyers", "Accounting", "Vice President"),
            3: Employee("Mark Jones", "IT", "Programmer"),
            4: Employee("Joy Rogers", "Manufacturing", "Engineer"),
        }

        lookup_employee(mock_employees)

        captured = self.capsys.readouterr()
        assert captured.out.count("ERROR: Employee 1 does not exist.") == 1

    def test_lookup_employee_should_successfully_lookup_employee(
        self, monkeypatch: MonkeyPatch
    ) -> None:
        def mock_input(prompt: str) -> str:
            assert prompt == "Enter an employee ID: "
            return "1"

        monkeypatch.setattr("builtins.input", mock_input)

        mock_employees: dict[int, Employee] = {
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            2: Employee("Mark Jones", "IT", "Programmer"),
            3: Employee("Joy Rogers", "Manufacturing", "Engineer"),
        }

        lookup_employee(mock_employees)

        captured = self.capsys.readouterr()
        assert (
            captured.out.count(
                "Name: Susan Meyers\nDepartment: Accounting\nJob Title: Vice President"
            )
            == 1
        )

    def test_find_available_id_should_be_correct_before_insertion(self) -> None:
        mock_employees = {
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            2: Employee("Mark Jones", "IT", "Programmer"),
            3: Employee("Joy Rogers", "Manufacturing", "Engineer"),
        }

        id = find_available_id(mock_employees)
        assert id == 4

    def test_find_available_id_should_return_proper_id_to_reuse(self) -> None:
        mock_employees = {
            4: Employee("Joy Rogers", "Manufacturing", "Engineer"),
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            3: Employee("Mark Jones", "IT", "Programmer"),
        }

        assert find_available_id(mock_employees) == 2

    def test_add_employee_should_add_employee_with_proper_id(
        self, monkeypatch: MonkeyPatch
    ) -> None:
        inputs = iter(["Sandy Smith", "AR", "Reimbursement Specialist"])

        def mock_input(prompt: str) -> str:
            if "name" in prompt:
                assert prompt == "Enter employee name: "
            elif "department" in prompt:
                assert prompt == "Enter department: "
            elif "job_title" in prompt:
                assert prompt == "Enter job title: "

            return next(inputs)

        monkeypatch.setattr("builtins.input", mock_input)

        mock_employees = {
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            2: Employee("Mark Jones", "IT", "Programmer"),
            3: Employee("Joy Rogers", "Manufacturing", "Engineer"),
        }

        assert len(mock_employees) == 3
        assert 4 not in mock_employees

        add_employee(mock_employees)

        assert len(mock_employees) == 4
        assert 4 in mock_employees
        assert mock_employees[4].name == "Sandy Smith"
        assert mock_employees[4].department == "AR"
        assert mock_employees[4].job_title == "Reimbursement Specialist"

    def test_change_employee_should_display_error_if_no_employees_exist(self) -> None:
        change_employee({})
        captured = self.capsys.readouterr()
        assert captured.out.count("ERROR: No employees exist.") == 1

    def test_change_employee_should_raise_error_when_employee_does_not_exist(
        self, monkeypatch: MonkeyPatch
    ) -> None:
        def mock_input(prompt: str) -> str:
            assert prompt == "Enter an employee ID: "
            return "1"

        monkeypatch.setattr("builtins.input", mock_input)

        mock_employees: dict[int, Employee] = {
            2: Employee("Susan Meyers", "Accounting", "Vice President"),
            3: Employee("Mark Jones", "IT", "Programmer"),
            4: Employee("Joy Rogers", "Manufacturing", "Engineer"),
        }

        change_employee(mock_employees)

        captured = self.capsys.readouterr()
        assert captured.out.count("ERROR: Employee 1 does not exist.") == 1

    def test_change_employee_should_edit_employee_data(
        self, monkeypatch: MonkeyPatch
    ) -> None:
        inputs = iter(["1", "Susan Smith", "Marketing", "President"])

        def mock_input(prompt: str) -> str:
            if "id" in prompt:
                assert prompt == "Enter an employee ID: "
            elif "name" in prompt:
                assert prompt == "New name: "
            elif "department" in prompt:
                assert prompt == "New department: "
            elif "job_title" in prompt:
                assert prompt == "New job title: "

            return next(inputs)

        monkeypatch.setattr("builtins.input", mock_input)

        mock_employees = {
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            2: Employee("Mark Jones", "IT", "Programmer"),
            3: Employee("Joy Rogers", "Manufacturing", "Engineer"),
        }

        assert mock_employees[1].name == "Susan Meyers"
        assert mock_employees[1].department == "Accounting"
        assert mock_employees[1].job_title == "Vice President"

        change_employee(mock_employees)

        assert mock_employees[1].name == "Susan Smith"
        assert mock_employees[1].department == "Marketing"
        assert mock_employees[1].job_title == "President"

    def test_menu_exit_option_should_exit(
        self, mock_load_employees: Any, mock_open_file: Any, monkeypatch: MonkeyPatch
    ) -> None:
        def mock_input(prompt: str) -> str:
            assert prompt == "Enter your choice: "
            return "5"

        monkeypatch.setattr("builtins.input", mock_input)

        main()

        captured = self.capsys.readouterr()
        assert captured.out.count("Employee Management System") == 1
        assert captured.out.count("1. Look up an employee") == 1
        assert captured.out.count("2. Add new employee") == 1
        assert captured.out.count("3. Edit employee") == 1
        assert captured.out.count("4. Delete employee") == 1
        assert captured.out.count("5. Exit") == 1

    def test_invalid_menu_option_input_should_display_error_message_and_display_menu(
        self,
        mock_load_employees: Any,
        mock_save_employees: Any,
        monkeypatch: MonkeyPatch,
    ) -> None:
        inputs = iter(["0", "5"])

        def mock_input(prompt: str) -> str:
            assert prompt == "Enter your choice: "
            return next(inputs)

        monkeypatch.setattr("builtins.input", mock_input)

        main()

        captured = self.capsys.readouterr()
        assert captured.out.count("ERROR: Please enter a valid menu option.") == 1
        assert captured.out.count("Employee Management System") == 1
        assert captured.out.count("1. Look up an employee") == 2
        assert captured.out.count("2. Add new employee") == 2
        assert captured.out.count("3. Edit employee") == 2
        assert captured.out.count("4. Delete employee") == 2
        assert captured.out.count("5. Exit") == 2

    @pytest.mark.parametrize("choice", ["1", "2", "3", "4"])
    def test_main_menu_options_should_output_menu_items_correctly(
        self,
        choice: list[str],
        mock_add_employee: Any,
        mock_change_employee: Any,
        mock_load_employees: Any,
        mock_lookup_employee: Any,
        mock_save_employees: Any,
        monkeypatch: MonkeyPatch,
    ) -> None:
        inputs = iter([choice, "5"])

        def mock_input(prompt: str) -> str | list[str]:
            assert prompt == "Enter your choice: "
            return next(inputs)

        monkeypatch.setattr("builtins.input", mock_input)

        main()

        captured = self.capsys.readouterr()
        assert captured.out.count("Employee Management System") == 1
        assert captured.out.count("1. Look up an employee") == 2
        assert captured.out.count("2. Add new employee") == 2
        assert captured.out.count("3. Edit employee") == 2
        assert captured.out.count("4. Delete employee") == 2
        assert captured.out.count("5. Exit") == 2
