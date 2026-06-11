import pytest
from main import main


class TestMain:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys):
        self.capsys = capsys

    def test_execution_block(self,monkeypatch):
        monkeypatch.setattr('main.main', lambda: None)
        

    def test_menu_exit(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '5')
        main()
        captured = self.capsys.readouterr()
        assert "1. Look up an employee" in captured.out
        assert "5. Exit" in captured.out

    def test_invalid_input(self, monkeypatch):
        inputs = iter(['9', '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 
        main()
        captured = self.capsys.readouterr()
        assert "ERROR: Please enter a valid menu option." in captured.out
    
    @pytest.mark.parametrize("choice", ['1', '2', '3', '4'])
    def test_menu_options(self, choice, monkeypatch):
        inputs = iter([choice, '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        main()
