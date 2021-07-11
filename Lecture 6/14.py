def isPangram(s):
    t = ''
    for i in range(len(s)):
        if s[i].isalnum():
            t += s[i]
    l = set()
    for i in range(len(t)):
        l.add(t[i])
    if len(l) >= 26:
        return 'The input string is pangram'
    else:
        return 'The input string is not pangram' 
s = input().lower()
print(isPangram(s))