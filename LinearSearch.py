def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
print("Linear Search:", linear_search(arr, target))
