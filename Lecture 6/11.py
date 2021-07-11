def isPerfect(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    if n == sum(div):
        return 'The input number is perfect number'
    else:
        return 'The input number is not perfect number'
n = int(input())
print(isPerfect(n))