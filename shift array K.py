def rotate_array():
    N = int(input())
    arr = list(map(int,input().split()))
    K = int(input())
    K = K % N
    rotated_array = arr[-K:] + arr[:-K]
    print(" ".join(map(str, rotated_array)))
rotate_array()
