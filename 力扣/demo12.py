"""
剑指 Offer 12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。



示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
"""

class Solution:
    def exist(self, board, word):
        if board:
            m = len(board)  # m行
        if board[0]:
            n = len(board[0])  # n列
        for i in range(m):
            for j in range(n):
                path_list = []
                if board[i][j] == word[0]:
                    path_list.append((i, j))
                    now_i = i
                    now_j = j
                    if len(word) ==1:
                        return True
                    else:
                        while True:
                            if now_i+1 < m and (now_i + 1, now_j) not in path_list and board[now_i+1][now_j] == word[len(path_list)]:   # 下
                                path_list.append((now_i + 1, now_j))
                                now_i = now_i + 1
                                if len(path_list) == len(word):
                                    return True

                            elif now_i-1 > -1 and (now_i - 1, now_j) not in path_list and board[now_i-1][now_j] == word[len(path_list)]:     # 上
                                path_list.append((now_i - 1, now_j))
                                now_i = now_i - 1
                                if len(path_list) == len(word):
                                    return True

                            elif now_j+1 < n and (now_i, now_j + 1) not in path_list and board[now_i][now_j+1] == word[len(path_list)]:     # 右
                                path_list.append((now_i, now_j + 1))
                                now_j = now_j + 1
                                if len(path_list) == len(word):
                                    return True

                            elif now_j-1 > -1 and (now_i, now_j - 1) not in path_list and board[now_i][now_j-1] == word[len(path_list)]:     # 左
                                path_list.append((now_i, now_j - 1))
                                now_j = now_j - 1
                                if len(path_list) == len(word):
                                    return True
                            else:   # 无
                                break
                            print(path_list)

        return False


if __name__ == "__main__":
    a = [
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]
    ]
    targe = "AAB"
    solution = Solution()
    print(solution.exist(a,targe))










