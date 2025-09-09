
# def madlibs():
#     # ask the user for a name
#     youtuber_input = input("Enter a YouTuber: ")
#     youtuber = youtuber_input.capitalize()
#
#     # string concatenation (aka how to put strings together)
#     print("Subscribe to " + youtuber)
#     print("Subscribe to {}".format(youtuber)) #takes what's inside .format() and put into {}
#     print(f"Subscribe to {youtuber} !")
#
# madlibs() # ctrl + / to # all selected lines


adj = input("Enter a Adjective: ")
verb1 = input("Enter a Verb: ")
verb2 = input("Enter another Verb: ")
famous_person = input("Enter a Famous person: ")

madlib = (f"Computer programing is so {adj}! It makes me so \
excited all the time because I love to {verb1}. Stay \
hydrated and {verb2} like you are {famous_person}")

print(madlib)
