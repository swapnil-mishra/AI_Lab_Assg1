import unittest
from task4_compare import main as compare_main


class TestCompareSmoke(unittest.TestCase):
    def test_runs(self):
        # just ensure the compare script runs without exception
        compare_main()


if __name__ == '__main__':
    unittest.main()
