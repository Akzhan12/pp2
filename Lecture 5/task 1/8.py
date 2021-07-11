with open('test.txt', encoding='utf8') as f:
    x = f.read().split()
print(max(x, key=len))