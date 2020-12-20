"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。



示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."


限制：

0 <= s 的长度 <= 10000

通过次数121,856提交次数1
"""


class Solution:
    def replaceSpace(self, s):
        need_str = ""
        for i in s:
            if i == " ":
                need_str += "%20"
            else:
                need_str += i
        return need_str


if __name__ == "__main__":
    s = "We are happy."
    solution = Solution()
    print(solution.replaceSpace(s))
