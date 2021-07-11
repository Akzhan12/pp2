def hyphen_sep(s):
    x = sorted(s)
    print(*x, sep = '-')
hyphen_sep(input().split('-'))