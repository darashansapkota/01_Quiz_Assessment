# Ask the user if they have played before
show_instructions = input("Have you played Quiz before?") .lower()

# if yes, output "program continues"
if show_instructions.lower() == "yes":
    print("program Continues")

elif show_instructions.lower() == "y":
    print("program Continues")

# if no output 'display instructions'
elif show_instructions.lower() == "no":
    print("Display Instructions")

elif show_instructions.lower() == "n":
    print("Display Instructions")

else:
    print("Please enter Yes or no")
