import unittest

# https://leetcode.com/problems/longest-consecutive-sequence/solutions/4932112/no-nested-loops-a-true-o-n-time-algorithm/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            x = table.get(num - 1, 0)
            y = table.get(num + 1, 0)
            val = x + y + 1
            table[num - x] = val
            table[num + y] = val
            maxval = max(maxval, val)
        return maxval


class TestSolution(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.longestConsecutive([1,2,3]), 3, 'The longest consecutive length is wrong.')

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.longestConsecutive([10,20,30,11,9]), 3, 'The longest consecutive length is wrong.')

if __name__ == '__main__':
    unittest.main()