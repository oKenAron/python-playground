# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def cdn_max_include(root: TreeNode | None, max_num = None):
    if root.left == None:
        return 1, 0
    sub_left, left_max = cdn_max_include(root.left, max_num)
    if root.right == None:
        sub_right = 0
        val_right = 0
        right_max = 0
    else:
        sub_right, right_max = cdn_max_include(root.right, max_num)
        val_right = root.right.val
    max_num = max(left_max, right_max, root.left.val, val_right)
    return sub_left + sub_right + 1 if max_num <= root.val else sub_left + sub_right, max_num

class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans, _ = cdn_max_include(root = root, max_num = 0)
        return ans
