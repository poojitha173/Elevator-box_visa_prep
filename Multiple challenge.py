def count_multiples(n):
    count_3 = n // 3
    count_5 = n // 5
    count_15 = n // 15
    return count_3 + count_5 - count_15
n = int(input().strip())
print(count_multiples(n))
