
import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def depthFirstConcat(thisPath, total, node):
            thisPath = thisPath + str(node.val)

            if node.left: 
                total = depthFirstConcat(thisPath, total, node.left)

            if node.right: 
                total = depthFirstConcat(thisPath, total, node.right)

            if node.left == None and node.right == None:
                total += int(thisPath)

            return total

        return depthFirstConcat("", 0, root)    



class TestSolution(unittest.TestCase):

    def test_1(self):
        root = TreeNode(4, None, None)
        solution = Solution()
        self.assertEqual(solution.sumNumbers(root), 4, 'The sum is wrong.')

    def test_2(self):
        left = TreeNode(2, None, None)
        root = TreeNode(4, left, None)

        solution = Solution()
        self.assertEqual(solution.sumNumbers(root), 42, 'The sum is wrong.')

    def test_3(self):
        left = TreeNode(2, None, None)
        right = TreeNode(9, None, None)
        root = TreeNode(4, left, right)

        solution = Solution()
        self.assertEqual(solution.sumNumbers(root), 42+49, 'The sum is wrong.')

    def test_4(self):
        right2 = TreeNode(1, None, None)
        left = TreeNode(2, None, right2)
        right = TreeNode(9, None, None)
        root = TreeNode(4, left, right)

        solution = Solution()
        self.assertEqual(solution.sumNumbers(root), 421+49, 'The sum is wrong.')


if __name__ == '__main__':
    unittest.main()

