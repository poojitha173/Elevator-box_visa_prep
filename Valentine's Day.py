def max_chocolates(x,y):
    return x // y
if __name__ == "__main__":
    x,y = map(int, input().split())
    print(max_chocolates(x,y))
