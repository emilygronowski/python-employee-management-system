import pytest
from main import main
import runpy

class TestMain:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys):
        self.capsys = capsys

    def test_execution_block(self,monkeypatch):
        monkeypatch.setattr('main.main', lambda: None)
        runpy.run_path('main.py')

    def test_menu_exit(self, monkeypatch):
        # Mock input to '5' so the program exits
        monkeypatch.setattr('builtins.input', lambda _: '5')
        main()
        captured = self.capsys.readouterr()
        # Verification that menu options get printed
        assert "1. Look up an employee" in captured.out
        assert "5. Exit" in captured.out

    def test_invalid_input(self, monkeypatch):
        # Iterator for '9' (invalid) then '5' (exit)
        inputs = iter(['9', '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 
        main()
        captured = self.capsys.readouterr()
        # Verification that error message gets printed
        assert "ERROR: Please enter a valid menu option." in captured.out
    
    # Tests for options 1, 2, 3, and 4
    @pytest.mark.parametrize("choice", ['1', '2', '3', '4'])
    def test_menu_options(self, choice, monkeypatch):
        # Iterator for [selected_option, exit]
        inputs = iter([choice, '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        main()
