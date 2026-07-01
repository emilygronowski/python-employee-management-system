import builtins
from typing import Any
from unittest.mock import call, mock_open

import pytest
from pytest import CaptureFixture, MonkeyPatch

from app.main import load_employees, main
from app.models.employee import Employee


class TestMain:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys: CaptureFixture[str]) -> None:
        self.capsys = capsys

    @pytest.fixture
    def mock_employees(self, monkeypatch: MonkeyPatch) -> None:
        mock_employees: dict[int, Employee] = {
            1: Employee("Susan Meyers", "Accounting", "Vice President"),
            2: Employee("Mark Jones", "IT", "Programmer"),
            3: Employee("Joy Rogers", "Manufacturing", "Engineer"),
        }

        def mock_load_employees():
            return mock_employees

        monkeypatch.setattr("app.main.load_employees", mock_load_employees)

    @pytest.fixture
    def mock_open_file(self, monkeypatch: MonkeyPatch) -> Any:
        mock_open_file = mock_open()
        monkeypatch.setattr(builtins, "open", mock_open_file)
        return mock_open_file

    def test_load_employees_should_return_empty_dictionary(self):
        employees = load_employees()
        assert not employees

    @pytest.mark.parametrize("choice", ["1", "2", "3", "4"])
    def test_process_menu_options(
        self,
        choice: list[str],
        mock_employees: None,
        mock_open_file: Any,
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

        mock_open_file.assert_called_once_with("employees.csv", "w")
        assert mock_open_file().write.call_count == 3

        expected_calls = [
            call("1,Susan Meyers,Accounting,Vice President\n"),
            call("2,Mark Jones,IT,Programmer\n"),
            call("3,Joy Rogers,Manufacturing,Engineer\n"),
        ]

        mock_open_file().write.assert_has_calls(expected_calls, any_order=False)

    def test_menu_exit_option_should_exit(
        self, mock_employees: None, mock_open_file: Any, monkeypatch: MonkeyPatch
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

        mock_open_file.assert_called_once_with("employees.csv", "w")
        assert mock_open_file().write.call_count == 3

        expected_calls = [
            call("1,Susan Meyers,Accounting,Vice President\n"),
            call("2,Mark Jones,IT,Programmer\n"),
            call("3,Joy Rogers,Manufacturing,Engineer\n"),
        ]

        mock_open_file().write.assert_has_calls(expected_calls, any_order=False)

    def test_invalid_menu_option_input_should_display_error_message(
        self, mock_employees: None, mock_open_file: Any, monkeypatch: MonkeyPatch
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

        mock_open_file.assert_called_once_with("employees.csv", "w")
        assert mock_open_file().write.call_count == 3

        expected_calls = [
            call("1,Susan Meyers,Accounting,Vice President\n"),
            call("2,Mark Jones,IT,Programmer\n"),
            call("3,Joy Rogers,Manufacturing,Engineer\n"),
        ]

        mock_open_file().write.assert_has_calls(expected_calls, any_order=False)
