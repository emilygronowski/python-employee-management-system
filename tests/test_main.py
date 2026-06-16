import pytest
from pytest import CaptureFixture, MonkeyPatch

from app.main import main


class TestMain:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys: CaptureFixture[str]) -> None:
        self.capsys = capsys

    @pytest.mark.parametrize("choice", ["1", "2", "3", "4"])
    def test_process_menu_options(
        self, choice: list[str], monkeypatch: MonkeyPatch
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

    def test_menu_exit_option_should_exit(self, monkeypatch: MonkeyPatch) -> None:
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

    def test_invalid_menu_option_input_should_display_error_message(
        self, monkeypatch: MonkeyPatch
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
