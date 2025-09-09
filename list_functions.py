
lucky_numbers = [4, 8, 15, 16, 23, 42]
               # 5  6  7   8   9   10
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]
            # 0        1       2       3       4
friends.extend(lucky_numbers)
friends.insert(8, "Creed") # inserts before 16

print(lucky_numbers)
print(friends)



n1 = int(input("Enter a number: "))
n2 = input("Enter another number: ")
n3 = input("Enter another number: ")
n4 = input("Enter another number: ")
n5 = input("Enter another number: ")

nums = [n1, n2, n3, n4, n5]
nums.sort()
print(nums)