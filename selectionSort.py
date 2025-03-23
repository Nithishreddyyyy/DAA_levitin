# 02 Using Brute Force implement Selection Sort
def selectionSort(arr, n):
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if (arr[j] < arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]


arr = [12, 30, 43, 56]
selectionSort(arr, len(arr))
print(arr)
