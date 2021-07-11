def max_of_3(a, b, c):
    return max(max(a, b), c)
a, b, c = map(int, input().split())
print(max_of_3(a, b, c))