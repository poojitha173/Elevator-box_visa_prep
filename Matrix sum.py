def mystical_matrix_sums():
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    row_sums = [0] * N
    col_sums = [0] * N
    for i in range(N):
        for j in range(N):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]
    result = []
    for i in range(N):
        result.append(row_sums[i] + col_sums[i])
    print(" ".join(map(str, result)))
mystical_matrix_sums()
