"""
未完成
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
"""


class Solution:
    def minArray(self, numbers):
        """
        二分
        mid值小于前和后则为目标值
        """
        if not numbers:
            return None
        left = 0
        right = len(numbers) - 1
        if numbers[left] < numbers[right]:
            return numbers[left]
        while True:
            mid = (left + right)//2
            if mid == left or mid == right:
                return min(numbers[left],numbers[right])
            if numbers[mid] < numbers[mid-1] and numbers[mid] < numbers[mid+1]:
                return numbers[mid]
            elif numbers[mid] > numbers[mid-1] and numbers[mid] > numbers[mid+1]:
                return numbers[mid+1]
            else:
                if numbers[mid] >= numbers[right]:
                    left = mid + 1
                elif numbers[mid] <= numbers[left]:
                    right = mid - 1
                elif numbers[mid] == numbers[left] and numbers[mid] == numbers[right]:
                    return numbers[mid]


        # if numbers[left] < numbers[right]:
        #     return numbers[left]
        # for i in range(len)

if __name__ == "__main__":
    a = [10, 1, 10, 10, 10]
    solution = Solution()
    print(solution.minArray(a))