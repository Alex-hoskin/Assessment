print("🟣🔵  number sequences 🔵🟣")

name = input("Please enter your name ")
print(name)

# loop for testing purposes

while True:
    want_instructions = input("Do you want to read the instructions? yes/no ").lower()

    # checks users enter yes (y) or no (n)
    if want_instructions == "yes" or want_instructions == "y":
        print("you chose yes")
    elif want_instructions == "no" or want_instructions == "n":
        print("you chose yes")
    else:
        print("please answer yes or no")


