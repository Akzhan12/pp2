def mult_of_list(list_name):
    ans = 1
    for i in list_name: ans *= i
    return ans
list = [int(i) for i in input().split()]
print(mult_of_list(list))