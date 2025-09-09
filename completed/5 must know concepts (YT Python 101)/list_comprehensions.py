
x = [i * 2 for i in range(10)] # i * 2 'for' each item in i, i is 'in' the range of 10

print(x)


print()
x = [[j * 3 for j in range(5)]  for i in range(10)]# j * 3 'for' each item in j, j is 'in' the range of 5, and i
print(x)


print()
x = [i for i in range(10) if i % 3 == 0] # only print 'if' i is divisible by 3
print(x)