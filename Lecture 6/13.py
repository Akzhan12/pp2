  
def pascal(n):
    for i in range(1, n + 1):
        num = 1
        for j in range(1, i + 1):
            print(num, end = ' ')
            num = int(num * (i - j) / j)
        print()
pascal(int(input()))