def unique_list(list):
    ans = []
    for i in list:
        if i not in ans: ans.append(i)
    return ans

list = list(map(int, input().split()))
print(unique_list(list))