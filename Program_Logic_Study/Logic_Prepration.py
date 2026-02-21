# 1. Two sum 
def two_sum(num, target):
    n = len(num)
    for i in range(n):
        for j in range(i+1, n):
            if num[i]+num[j] == target:
                return[i,j]
    return []
num = [2,5,6,7,8,10]
target = 13
result = two_sum(num, target)
print(result)