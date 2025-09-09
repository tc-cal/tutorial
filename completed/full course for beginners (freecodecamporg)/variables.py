
character_name = "John" #str
character_age = "35" #str
character_age_num = int(character_age) #1 converting str to int

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")
print("he really liked the name " +character_name + ", ")
print("but he wished he was " + str(character_age_num - 10) + " years old.")
#2 last line uses int of 35 from above to minus 10 first, as it's in brackets
#3 then it converts the int of 25 received back into str before printing


character_name = "John"
character_age = 35   # store as an integer directly

# WHEN DEALING W VARIABLES, USE F" OR .FORMAT(), IT'S CLEANER
print(f"There once was a man named {character_name},")
print(f"he was {character_age} years old.")
print(f"he really liked the name {character_name},")
print(f"but he wished he was {character_age - 10} years old.")
# single step vs 3 steps conversion of str to int to str