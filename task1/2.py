a = list(map(int, input().strip().split()))
min = 1000
for i in a:
    if i > 0 and i < min:
        min = i
    print(min)