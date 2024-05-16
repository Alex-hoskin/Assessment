# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question)
        # checks users enter yes (y) or no (n)
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes or no")


# Main routine
want_instructions = yes_no("Do you want the instructions yes/no ")
print(f"you chose {want_instructions}")
