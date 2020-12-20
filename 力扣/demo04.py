"""
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。



限制：

0 <= n <= 1000

0 <= m <= 1000


"""


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if matrix:
            m = len(matrix)  # 行数
        else:
            return False
        if matrix[0]:
            n = len(matrix[0])  # 列数
        else:
            return False
        """
        右上角开始，小于则左，大于下
        初始x=n-1,y=0
        [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]]
        """
        x = n - 1  # 横
        y = 0  # 竖
        while x >= 0 and x < n and y >= 0 and y < m:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                x -= 1
            else:
                y += 1
        return False

        """
        逻辑转换二维为一维,二分查找
        总数量: m*n
        二位下表对应总数下表
        matrix[x][y] -> x = index // n   y = index % n
        """
        # left = 0
        # right = m * n - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     x = mid // n
        #     y = mid % n
        #     if matrix[x][y] == target:
        #         return True
        #     elif matrix[x][y] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False
