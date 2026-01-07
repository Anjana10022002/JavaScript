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
