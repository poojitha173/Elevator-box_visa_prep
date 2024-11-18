def transpose_matrix(matrix, n):
    transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return transposed
n = int(input().strip())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]
transposed_matrix = transpose_matrix(matrix, n)
for row in transposed_matrix:
    print(" ".join(map(str, row)))
