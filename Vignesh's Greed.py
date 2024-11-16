def max_triangle_perimeter():
    n = int(input())
    sticks =list(map(int,input().split()))
    sticks.sort(reverse=True)
    for i in range(n - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            print(sticks[i] + sticks[i + 1] + sticks[i + 2])
            return
    print(-1)
max_triangle_perimeter()
