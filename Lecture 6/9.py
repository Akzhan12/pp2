def is_prime(n):
    if n == 0 or n == 1: return False
    if n == 2 or n == 3: return True
    i = 2
    for i in range(2, n):
        if n % i == 0: return False
    return True
n = int(input())
if is_prime(n):
     print('Number {} is prime'.format(n))
else:
     print('Number {} is non prime'.format(n))