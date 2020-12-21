"""
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
"""


class Solution:
    def is_out(self, i, j, k):
        c = str(i)+str(j)
        total = 0
        for i in c:
            total += int(i)
        if total <= k:
            return True
        else:
            return False


    def movingCount(self, m, n, k):
        def search_for(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or not self.is_out(i, j, k) or (i, j) in path_list:
                return False
            path_list.append((i, j))
            search_for(i + 1, j)
            search_for(i - 1, j)
            search_for(i, j + 1)
            search_for(i, j - 1)

        path_list = []
        search_for(0, 0)
        return len(path_list)


if __name__ == "__main__":
    m = 2
    n = 3
    k = 1
    solution = Solution()
    print(solution.movingCount(m, n, k))