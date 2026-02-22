# 1. Two sum 
# def two_sum(num, target):
#     n = len(num)
#     for i in range(n):
#         for j in range(i+1, n):
#             if num[i]+num[j] == target:
#                 return[i,j]
#     return []
# num = [2,5,6,7,8,10]
# target = 13
# result = two_sum(num, target)
# print(result)

#  2. Kadane’s Algorithm – Maximum Subarray Sum
# def max_subarray(nums):
#     n = len(nums)
#     max_sum = nums[0]
#     for i in range(n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum += nums[j]
#             if current_sum > max_sum:
#                 max_sum = current_sum
#     return max_sum
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_subarray(nums))

# 3. 