import pytest
from unittest.mock import patch
from main import main


class TestMain:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys):
        self.capsys = capsys

    def test_main_exit(self):
        #test to input to return '5' to exit the program
        with patch('builtins.input', return_value='5'):
            main()
            captured = self.capsys.readouterr()

            #verification that menu options get printed
            assert "1. Look up an employee" in captured.out
            assert "5. Exit" in captured.out

    def test_invalid_input(self):
        #test to input an invalid menu option
        with patch('builtins.input', side_effect=['9', '5']): #return '9' first to trigger error message, then '5' to exit the program
            main()
            captured = self.capsys.readouterr()

            #verification that error message gets printed
            assert "ERROR: Please enter a valid menu option." in captured.out
    
    #tests for options 1,2,3, and 4
    @pytest.mark.parametrize("choice", ['1', '2', '3', '4'])
    def test_menuUoptions(self, choice):
        with patch('builtins.input', side_effect=[choice, '5']):
            main()
