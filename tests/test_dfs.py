import unittest
from task3_dfs import dfs_limit


class TestDFS(unittest.TestCase):
    def test_dfs_near_goal(self):
        start = ('1','2','3','4','5','6','7','B','8')
        res = dfs_limit(start, limit=5)
        self.assertTrue(res['found'])
        self.assertEqual(res['steps'], 1)


if __name__ == '__main__':
    unittest.main()
