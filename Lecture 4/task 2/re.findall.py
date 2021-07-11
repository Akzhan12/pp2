  import re
print(*re.findall('[AEIOUaeiou]{2,}', input()), sep = '\n')