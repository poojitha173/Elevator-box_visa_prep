def calculate_score(total_points, passed_cases):
    points_per_case = total_points // 10
    return points_per_case * passed_cases
if __name__== "__main__":
    T = int(input())
    for _ in range(T):
        X, N = map(int, input().split())
        score = calculate_score(X,N)
        print(score)
