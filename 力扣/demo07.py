"""
未完成

剑指 Offer 07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。



例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


限制：

0 <= 节点个数 <= 5000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        preorder    前序遍历    根->左->右
        inorder     中序遍历    左->根->右
        perorder[0]为最上层节点
        inorder在perorder[0]前面的为树左侧，后面的为树右侧
        """
        node = TreeNode(property[0])
        left = inorder.index(node.val) - 1
        if left >= 0:
            node.left = TreeNode(inorder[left])
        right = inorder.index(node.val) + 1
        if right < len(inorder):
            node.left = TreeNode(inorder[right])