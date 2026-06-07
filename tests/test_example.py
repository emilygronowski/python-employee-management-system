from scripts import sum


class TestExample:
    def test_sum(self):
        assert sum(1, 1) == 2
        assert sum(2, 2) == 4
        assert sum(3, 3) == 6
