X, Y, Z = map(int,input().split())
remaining_capacity = Z - Y
if remaining_capacity < 0:
    print(0)
else:
    max_mangoes = remaining_capacity // X
    print(max_mangoes)
