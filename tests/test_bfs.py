import unittest
from task2_bfs import bfs


class TestBFS(unittest.TestCase):
    def test_bfs_near_goal(self):
        # a state one move away: swap 8 and B
        start = ('1','2','3','4','5','6','7','B','8')
        res = bfs(start)
        self.assertTrue(res['found'])
        self.assertEqual(res['steps'], 1)


if __name__ == '__main__':
    unittest.main()
