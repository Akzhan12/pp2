from sys import stdin

def cmp(x):
    return(-x[0], x[1])

inp = str(stdin.read()).split()
d = {}
for i in inp:
    d[i] = d.get(i, 0) + 1
d = [(x, y) for y, x in d.items()]
d.sort(key = cmp)
for i in range(len(d)):
    print(d[i][1])