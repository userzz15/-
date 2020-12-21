import random


def bubble_sort(arr, size):
    """冒泡排序"""
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def select_sort(arr, size):
    """选择排序"""
    for i in range(size - 1):
        temp = i
        for j in range(i+1, size):
            if arr[temp] > arr[j]:
                temp = j
        if temp != i:
            arr[i], arr[temp] = arr[temp], arr[i]


def insert_sort(arr, size):
    """插入排序"""
    for i in range(1, size):
        j = i
        while j-1 > -1 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


def quick_sort(arr, start, end):
    """快速排序"""
    if start >= end:
        return
    left = start
    right = end
    temp = arr[left]
    while left < right:
        while left < right and arr[right] > temp:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= temp:
            left += 1
        arr[right] = arr[left]
    arr[right] = temp
    quick_sort(arr, start, right)
    quick_sort(arr, right+1, end)


def merge(arr, start, mid ,end):
    left = start
    right = mid + 1
    temp = []
    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= end:
        temp.append(arr[right])
        right += 1
    arr[start:end+1] = temp



def merge_sort(arr, start, end):
    """归并排序"""
    if start >= end:
        return
    mid = (start + end)//2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, mid, end)


def heap(arr, start, end):
    i = start
    j = 2 * i + 1
    temp = arr[i]
    while i <= (end-1)//2:
        if j+1 <= end and arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],arr[j]
        if temp < arr[j]:
            arr[i] = arr[j]
        else:
            arr[i] = temp
            break
        i = j
        j = 2 * i + 1
    arr[i] = temp


def heap_sort(arr, size):
    """堆排序"""
    for i in range((size-1)//2, -1, -1):
        heap(arr, i, size)

    for i in range(size, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap(arr, 0, i-1)





def run():
    arr = list(range(10))
    size = len(arr)
    random.shuffle(arr)
    print(arr)
    # bubble_sort(arr, size)
    # select_sort(arr, size)
    # insert_sort(arr, size)
    # quick_sort(arr, 0, size-1)
    # merge_sort(arr, 0, size-1)
    heap_sort(arr, size - 1)
    print(arr)



if __name__ == "__main__":
    run()
