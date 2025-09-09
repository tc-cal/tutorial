
name = input("Enter your name: ")
age = int(input("Enter your age: "))   # convert input to int

if age >= 30: # first condition
    print("Sorry " + name + ", you’re too old for this 😅")
else:
    sexy = input("Are you wearing a skirt? (yes/no): ")

    if sexy.lower() == "yes" or sexy.lower() == "y": # second condition
        print("Hello " + name + "! You so sexy!!")

    elif sexy.lower() == "no" or sexy.lower() == "n":
        print("Hello " + name + "! You so fineee~")

    else:
        print("Stop playing around honey.")
