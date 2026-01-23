"""
Program Logic explanation

1. Input the list of numbers (num)
2. Create a function count and pass num as parameter
3. Inside the function check whether the list is empty, if so return 0
4. Initialize a variable count to 0
5. Using for loop iterate through the list
6. Using if condition check the the number is greater than 0 and even
7. Increment the count if the condition is true
8. Return count
9. Call the function and pass num as argument
10. Print count
"""

def count(num):
    if num == []:
        return 0
    count = 0
    for x in num:
        if x > 0 and x % 2 == 0:
            count += 1
    return count

num = [1,2,5,-10,7,8, 12]
count = count(num)
print("The count of positive even numbers is:", count)