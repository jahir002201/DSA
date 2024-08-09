def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
    return sorted_arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Counting Sort:", counting_sort(arr.copy()))
