
def complicated_function(x, y, z):
    print(x, y, z)
    pass

complicated_function(1, z = 2, y = 3) # must start w positional argument, then keyword argument after


print()
def complicated_function(x, y, z = none): # does not require all positional argument
    print(x, y, z)
    pass

complicated_function(1, 3)