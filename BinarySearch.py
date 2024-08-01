def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = sorted([64, 34, 25, 12, 22, 11, 90])
target = 22
print("Binary Search:", binary_search(arr, target))
