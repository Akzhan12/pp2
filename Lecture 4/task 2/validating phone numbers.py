import re
for i in range(int(input())):
    print('YES' if re.match('[789]\d{9}$', input()) else 'NO')