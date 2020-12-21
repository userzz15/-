"""
剑指 Offer 14- I. 剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
"""


class Solution:
    def cuttingRope(self, n):
        rope_dict = {
            1: [1],
            2: [1, 1],
            3: [1, 2],
            4: [2, 2],
        }
        if n < 5:
            rope_list = rope_dict[n]
            res = 1
            for i in rope_list:
                res *= i
            return res
        else:
            for i in range(5, n+1):
                res1 = 1
                res2 = 1
                rope_list1 = rope_dict[(n-2)]
                rope_list1.append(2)
                for i in rope_list1:
                    res1 *= i

                rope_list2 = rope_dict[(n-3)]
                rope_list2.append(3)
                for i in rope_list2:
                    res2 *= i

                if res1 > res2:
                    rope_dict[n] = rope_list1
                    res = res1
                else:
                    rope_dict[n] = rope_list2
                    res = res2

            return res
