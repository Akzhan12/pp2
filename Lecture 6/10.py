def even_list(list):
    ans = []
    for i in list:
        if i % 2 == 0: ans.append(i)
    return ans

list = [int(i) for i in input().split()]
print(even_list(list))