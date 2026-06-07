import pytest


from main import main


class TestMain:
    @pytest.fixture(autouse=True)
    def _capsys(self, capsys):
        self.capsys = capsys

    def test_main(self):
        main()
        captured = self.capsys.readouterr()
        assert captured.out == "Hello World\n20\n"
