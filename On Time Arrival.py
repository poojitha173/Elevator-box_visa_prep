T = int(input())
results = []
for _ in range(T):
    X = int(input())
    if X >= 30:
        results.append("YES")
    else:
        results.append("NO")
print("\n".join(results))
