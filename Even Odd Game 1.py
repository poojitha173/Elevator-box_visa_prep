def find_winner(n):
    digit_sum = sum(int(digit) for digit in n)
    if digit_sum % 2 == 0:
        return "Vignesh"
    else:
        return "Charan"
n = input().strip()
print(find_winner(n))
