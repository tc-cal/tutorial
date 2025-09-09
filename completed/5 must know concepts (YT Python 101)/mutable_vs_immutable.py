
x = (1, 2) # () are immutable/unchangeable
y = x # value of x now stored in y

x = (1, 2, 3) # assigned new value to x
print(x, y) # x is new value but y was prev stored


print()
x = [9, 8] # [] are mutable/changeable
y = x # even though x now stored in y, still mutable

x[0] = 100 # assigned x0 from 9 to now 100
x[1] = 200
print(x, y) # as x0 x1 got changed, y got changed


print()
def get_largest_numbers(numbers, n):
    numbers.sort()

    return numbers [-n:]

nums = [2, 3, 4, 1, 34, 123, 321, 1]

print(nums)
largest = get_largest_numbers(nums, 1)
print(nums)
print(largest)
