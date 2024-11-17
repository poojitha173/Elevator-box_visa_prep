def reduce_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result
s = input("")
if 1 <= len(s) < 100:
    print(reduce_string(s))
else:
    print("Invalid input.String length must be between 1 and 100.")
