
def flirty_game():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Early exit if age condition not met
    if age >= 30:
        print("Sorry " + name + ", you’re too old for this game 😅")
        return   # stops the function here

    # Only runs if age < 30
    sexy = input("Are you wearing a skirt? (yes/no): ")

    if sexy.lower() in ["yes", "y"]: # converts answer to lower case then compares if match with any conditions 'in' ()
        print("Hello " + name + "! You so sexy!!")

    elif sexy.lower() in ["no", "n"]:
        print("Hello " + name + "! You so fineee~")

    else:
        print("Stop playing around honey.")

# TODO add "try again" message & more functions

# Run the game
flirty_game()
