# Program 1 : Sum of list elements
nums = [1, 2, 3, 4, 5]
total = 0

for n in nums:
    total += n

print("Sum:", total)

# Program 2 : Find maximum number
nums = [3, 8, 1, 6, 9]

max_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n

print("Maximum:", max_num)

#Program 3 : Count even numbers
nums = [1, 2, 3, 4, 5, 6]
count = 0

for n in nums:
    if n % 2 == 0:
        count += 1

print("Even count:", count)

#Program 4 : Reverse a list (without using reverse())
nums = [10, 20, 30, 40]
rev = []

for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])

print("Reversed list:", rev)

