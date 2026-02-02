# 1. Check eligible to vote (age ≥ 18)
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting")

# 2. Find largest of three numbers
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c = int(input("Enter the third number:"))
# if (a>b and a>c):
#     print(a, "is the largest")
# elif(b>a and b>c):
#     print(b, "is the largest")
# else:
#     print(c, "is the largest")


#3. Check leap year
# a = int(input("Enter the year:"))
# if (((a % 4 == 0) and (a % 100 != 0)) or ((a % 400 == 0))):
#     print(a, "is a leap year")
# else:
#     print(a, "is not a leap year")

# 4. Sum of First N Numbers
# n = int(input("Enter n:"))
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
# print("Sum is: ",sum)

# 5. Factorial of a number
# n = int(input("Enter the number: "))
# fact = 1
# for i in range (1, n+1):
#     fact = fact * i
# print("The factorial is: ", fact)

# 6. Reverse a string 
# n = int(input("Enter the number: "))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# print("Reverse of the numbeer is:", rev)


#  7. Count of digits
# n = int(input("Enter the number: "))
# count = 1
# while n > 1:
#     count += 1
#     n //= 10

# print("The count is ", count)

# 8. palindrome number 
# num = int(input("Enter the number: "))
# rev = 0
# temp = num
# while num>0:
#     digit = num % 10
#     rev = rev * 10 + digit 
#     num //= 10
# if temp == rev:
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")

# 9. Print numbers from N to 1
# n = int(input("Enter the number:"))
# for i in range(n, 0, -1):
#     print(i)

# 10. Sum of digits
# n = int(input("Enter the number: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit 
#     n //=10
# print("Sum:", sum)

# 11. Maximum in array
# n = [12,56,78,95,12,42]
# max_val = n[0]
# for i in range (1, len(n)):
#     if n[i] > max_val:
#         max_val = n[i]

# print("Maximum: ", max_val)

# 12. Minimaum in array 
# n = [98,5,65,89,6,45]
# min_val = n[0]
# for i in range(1, len(n)):
#     if n[i] < min_val:
#         min_val = n[i]
# print("Minimum: ", min_val)

# 13. search an element
# n = [98,5,65,89,6,45]
# target = 100
# found = False
# for i in range (0, len(n)):
#     if (n[i] == target):
#         found = True
#         break
# if found:
#     print("Element found")
# else:
#     print("Element not found")

# 14. Count Occurrences
# arr = [1,2,3,4,2,5,2,6]
# target = 2
# count = 0

# for i in arr:
#     if arr[i] == target:
#         count +=1

# print("Count:", count)

# 15. Find duplicate elements 
# arr = [1,3,5,3,6,8,9,7, 9, 7]
# duplicates = []
# for i in range(len(arr)):
#     for j in range(1+i, len(arr)):
#         if arr[i] == arr[j] and arr[i] not in duplicates:
#             duplicates.append(arr[i])
# print("Duplicates:", duplicates)

# arr = [1,2,3,4,5,6,7,1,3,4,2,5]
# dupli = []
# for i in range(len(arr)):
#     for j in range(1+i, len(arr)):
#         if arr[i] == arr[j] and arr[i] not in dupli:
#             dupli.append(arr[i])

# print("Duplicates:", dupli)

# 16. Second largest number 
# arr = [10,57,39,68,90,27]
# largest = arr[0]
# second_largest = -1
# for i in range(len(arr)):
#     if arr[i]>largest:
#         second_largest = largest
#         largest = arr[i]
#     elif second_largest > largest:
#         largest = second_largest
# print("Second largest:", second_largest)

# 17. Reverse an array
# arr = [1,2,3,4]
# reverse = []
# for i in range(len(arr)):
#     reverse = arr[::-1]
# print(reverse)

# arr = [1,2,3,4]
# left = 0
# right = len(arr) -1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left +=1
#     right -=1
# print("Reverse:",arr)

# 18. Sum of array elements
# arr = [1,2,3,4]
# sum = 0
# for i in range(len(arr)):
#     sum = sum + arr[i]
# print (sum)

# 19. Remove duplicates 
# arr = [1,2,3,4,5,6,7,1,3,4,2,5]
# set = set(arr)
# print(set)

# arr = [1,2,3,4,5,6,7,1,3,4,2,5]
# without_duplicates  = []
# for n in arr:
#     if n not in without_duplicates:
#         without_duplicates.append(n)
# print(without_duplicates)

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# merge = arr1 + arr2
# print(merge)

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# arr1.extend(arr2)
# print(arr1)