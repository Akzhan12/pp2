a = list(input().split())
for i in a:
    if int(i) == 0:
        a.remove(i)
        a.append(i)
    print(*a)