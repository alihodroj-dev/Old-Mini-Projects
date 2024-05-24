# variables
RM_checker = open("RM_Checker", "r")

# Solving
if RM_checker.read() == "false":
    pass_input = str(input("Please enter your password: "))
    checker1 = str(input("Alright. Would you like to save your password(y/n): "))
    if checker1 == "y":
        RM_checker_Write = open("RM_Checker", "w")
        RM_checker_Write.write("true")
else:
    print("You are logged in!!!")
    checker2 = str(input("Would you like to remove the remember me(y/n): "))
    if checker2 == "y":
        RM_checker_Write = open("RM_Checker", "w")
        RM_checker_Write.write("false")