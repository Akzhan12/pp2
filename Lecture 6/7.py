def low_up(s):
    cnt_up, cnt_low = 0, 0
    for i in s:
        if i.islower(): cnt_low += 1
        elif i.isupper(): cnt_up += 1
    print('Upper case:', cnt_up)
    print('Lower case:', cnt_low)
low_up(input())