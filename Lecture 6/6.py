def is_in_range(n, a, b):
    if a <= n <= b:
         return True
    else:
         return False
a, b = map(int, input().split())
n = int(input())
if is_in_range(n, a, b):
     print('{} is in range'.format(n))
else:
     print('{} is out of given range'.format(n))