def rotate_array_by_one(n, arr):
    rotated_array = arr[1:] + arr[:1]
    return rotated_array
n = int(input().strip())
arr = list(map(int, input().strip().split()))
result = rotate = rotate_array_by_one(n, arr)
print(" ".join(map(str, result)))
