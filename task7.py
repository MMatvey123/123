def find_smallest_missing(arr):
    n = len(arr)
    present = [False] * (n + 1)
    for i in range(n):
        if arr[i] > 0 and arr[i] <= n:
            present[arr[i]] = True
    for i in range(1, n + 1):
        if not present[i]:
            return i
    return n + 1
arr = [3, 4, 1]
print(find_smallest_missing(arr))