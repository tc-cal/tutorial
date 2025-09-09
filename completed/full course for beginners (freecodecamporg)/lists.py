import random
# TO SIMPLIFY, CAN CONSIDER CTRL+F OLD_FRIEND & CTRL+R OLD


old_friends = ["sean", "khanh", "daniel, JaCkIe, JAY"]
#                0        1        2        3    4 or-1
extra_friends = [name.strip() for name in old_friends[2].split(",")] # split the item at index 2 by comma + strip spaces
old_friends = old_friends[:2] + extra_friends # old_friend up to but not inc index 2 (sean, khanh), then + extra which are the 2 splited above

print(1.)
friends = [name.capitalize() for name in old_friends] # can call it anything, doesn't have to be name
# take each item in old_friends one by one, call it 'name' while I process it, then move to the next item
print(f"{friends[-1]}, {old_friends[1]}") # as this is formated into string, prints without []
print(friends[2:4]) # lists print with []

print(2.)
shuffled1 = old_friends[:] # used slicking : so old remains unshuffled
shuffled2 = old_friends[:]
random.shuffle(shuffled1)
random.shuffle(shuffled2)
print(shuffled1) # shuffled & old both remains non-capitalized
print(shuffled2)

print(3.)
print(old_friends)
old_friends[0] = "jACKOb" # assign new value to index 0
old_friends = [name.capitalize() for name in old_friends] # reassign old to capitalized
print(old_friends)



print(4.)
random = ["Blue", 2, False]
random.append(56)

print(random)