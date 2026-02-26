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

# 20. Merge two arrays
# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# merge = arr1 + arr2
# print(merge)

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# arr1.extend(arr2)
# print(arr1)

# 21. Reverse a string
# str = "abcdef"
# rev = ""
# for i in range(len(str)-1, -1, -1):
#     rev +=str[i]
# print("Reverse:", rev)

# str = "abcdef"
# print(str[::-1])

# 22. Palindrome string
# str = "malayalam"
# rev = ""
# for i in range(len(str)-1, -1, -1):
#     rev +=str[i]
# if str == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# 23. count for vowels
# str = "Anjana"
# vowels = "AEIOUaeiou"
# count = 0
# for i in str:
#     if i in vowels:
#         count += 1
# print ("Count:", count)

# str = "Anjanapr"
# vowels = "AEIOUaeiou"
# count = 0
# for i in str:
#     if i not in vowels:
#         count +=1
# print("Count:", count)

# 24. Count Frequency of Characters
# str = "aabcghdassana"
# freq = {}
# for s in str:
#     if s in freq:
#         freq[s] +=1
#     else:
#         freq[s] = 1
# print("Frequency:", freq)

# 25. Removing whitespaces 
# str = "Hello World"
# res = ""
# for s in str:
#     if s != " ":
#         res += s
# print("Result:", res)

# 26. Count words
# str = "I am currently studying python"
# count = 1

# for s in str:
#     if s == " ":
#         count +=1
# print("Count:", count)

# 27. Count consonants
# str = "Anjanaprs"
# vowels = "AEIOUaeiou"
# count = 0
# for s in str:
#     if s not in vowels:
#         count +=1
# print("Count:", count)

# 28. First non repeating character
# str = "abcdesfabcsd"
# freq = {}
# non_repeating = ""

# for s in str:
#     if s in freq:
#         freq[s] +=1
#     else:
#         freq[s] =1

# for s in str:
#     if freq[s] == 1:
#         non_repeating = s
#         break
# print ("First Non-Repeating:", non_repeating)

# 29. Reverse each word in a string 
# str = "I am currently studying python"
# rev = ""
# for s in str:
    


# 30. Anagram check
# str1 = "listen"
# str2 = "silents"
# freq1 = {}
# freq2 = {}

# for s in str1:
#     if s in freq1:
#         freq1[s] += 1
#     else:
#         freq1[s] = 1

# for s in str2:
#     if s in freq2:
#         freq2[s] +=1
#     else:
#         freq2[s] = 1

# if freq1 == freq2:
#     print("Anagram")
# else:
#     print("Not anagram")

# 31. Prime number
# n = 5
# is_prime = True
# if n <= 1:
#     is_prime = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")

# 32. Armstrong Number
# n = 153
# temp = n
# power = len(str(n))
# total = 0
# while temp > 0:
#     digit = temp % 10
#     total += digit ** power
#     temp //= 10
# if n == total:
#     print("Armstrong")
# else:
#     print("Not armstrong")

# 33. Find Missing Number (Array 1 to N)
# a = [1,3,4,5,6]
# n = len(a) + 1

# expected = n*(n+1)//2
# array_sum = sum(a)
# print("Missing:", expected - array_sum)

# 34. Move Zeros to End (VERY COMMON)

# arr = [1,4,0,9,3,5,0,7,0,4,0,2,1]
# pos = 0
# for i in range(1, len(arr)):
#     if arr[i] != 0:
#         arr[pos] = arr[i]
#         pos +=1
# while pos < len(arr):
#     arr[pos] = 0
#     pos +=1
# print(arr)

# 35. Find Intersection of Two Arrays
# arr1 = [1,2,3,4,5,6]
# arr2 = [5,6,7,8,9,0]
# result =[]

# for i in arr1:
#     if i in arr2 and i not in result:
#         result.append(i)
# print(result)

# 36. Check array is sorted 
# arr = [1,2,3]
# is_sorted = True
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         is_sorted = True
#         break
# if is_sorted:
#     print("The array is sorted")
# else:
#     print("The array is not sorted")

# 




# reverse a string
# a = "abcde"
# reversed = ""
# for s in a:
#     reversed = s + reversed
# print(reversed)

# # largest in an array 
# a = [10,6,5,95,89,45,54]
# largest = a[0]
# for i in range(len(a)):
#     if a[i] > largest:
#         largest = a[i]
# print(largest)

# remove duplicates in an array 
# a = [1,3,2,1,4,6,2,3]
# result = []
# for i in a:
#     if i not in result:
#         result.append(i)
# print(result)

# fibonacci series
# a = 0
# b = 1
# for i in range(5):
#     print(a)
#     a, b = b, a + b
    
# frequency of character
# a = "banana"
# freq ={}
# for ch in a:
#     if ch in freq:
#         freq[ch] +=1
#     else:
#         freq[ch] = 1
# print(freq)
    
# str1 = "listen"
# str2 = "silent"
# freq1 = {}
# freq2 = {}
# for ch in str1:
#     if ch in freq1:
#         freq1[ch] +=1
#     else:
#         freq1[ch] = 1

# for ch in str2:
#     if ch in freq2:
#         freq2[ch] += 1
#     else:
#         freq2[ch] = 1

# if freq1 == freq2:
#     print("Anagram")
# else:
#     print("Not Anagram")

# prime number check
# n = 5
# if n <= 1:
#     print("not prime")
# else:
#     is_prime = True
#     for i in range (2, n):
#         if n % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")

# Find second smallest elemnt
arr = [2,4,6,8,1,9]

smallest = float('inf')
second = float('inf')

for i in arr:
    if i < smallest:
        second = smallest
        smallest = i
    elif i < second and i != smallest:
        second = i
print("Smallest: ", second)