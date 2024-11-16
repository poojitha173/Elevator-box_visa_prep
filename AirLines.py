def min_new_planes(x, N):
    required_planes = (N + 99) // 100 
    return max(0, required_planes - x)
if __name__ == "__main__":
    x, N = map(int, input().split())
    print(min_new_planes(x, N))
