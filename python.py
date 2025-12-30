# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print("Reverse:", rev)

    
num = int(input("Enter the number: "))
temp = num
num = 0
while num > 0:
    digit = num % 10
    rev = digit * 10 + rev 
    num //= 10
if temp == rev:
    print("The number is palindrome ")
else:
    print("The number is not palindrome.")