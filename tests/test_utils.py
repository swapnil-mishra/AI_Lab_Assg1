import unittest
from utils import solvable, rand_state, fmt, neigh, GOAL


class TestUtils(unittest.TestCase):
    def test_goal_solvable(self):
        self.assertTrue(solvable(GOAL))

    def test_rand_state(self):
        s = rand_state()
        self.assertEqual(len(s), 9)
        self.assertTrue(solvable(s))

    def test_fmt(self):
        s = GOAL
        out = fmt(s)
        self.assertIn('1 2 3', out)

    def test_neigh(self):
        # blank at last position -> neighbors should exist
        s = GOAL
        n = neigh(s)
        self.assertTrue(len(n) >= 2)


if __name__ == '__main__':
    unittest.main()
