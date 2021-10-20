

# functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Main routine goes here...
show_instructions = yes_no("Have you played the game before? ")
print("You chose {}".format(show_instructions))

if show_instructions.lower() == "yes" or show_instructions == "y":
    print("program Continues")


elif show_instructions.lower() == "no" or show_instructions =="n":
     print("*** How to play***")
     print("the rules of game is here")


