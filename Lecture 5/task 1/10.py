with open('freq.txt', encoding='utf8') as f:
    d = {}
    x = f.read().split()
    for i in x:
        d[i] = 0
    for i in x:
        d[i] += 1
    for i in d:
        print(f'{i}: {d[i]}')