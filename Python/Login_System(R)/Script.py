# Functions
def login():
    for acc in accounts_file_read.readlines():
        accounts.append(str(acc))
    login_stopper = 0
    while login_stopper != 1:
        login_email = input("Email: ")
        login_password = input("Password: ")
        for info in accounts:
            if info == (login_email + "\n"):
                if accounts[accounts.index(info) + 1] == (login_password + "\n"):
                    print("Welcome " + accounts[accounts.index(info) + 2])
                    login_stopper = 1
def signup():
    accounts = []
    signup_stopper = 0
    while signup_stopper != 1:
        signup_name = str(input("Name: "))
        signup_email = str(input("Email: "))
        signup_password1 = str(input("Password: "))
        signup_password2 = str(input("Repeat-Password: "))
        for acc in accounts_file_read.readlines():
            accounts.append(str(acc))
        if signup_password1 == signup_password2:
            accounts.append("\n" + signup_email + "\n")
            accounts.append(signup_password1 + "\n")
            accounts.append(signup_name)
            signup_stopper = 1

# variables
accounts_file_read = open("Accounts", "r")
accounts = []
start_stopper = 0
# Start
print("WELCOME!!!")
while start_stopper != 1:
    choice1 = str(input("Login or Sign-up: "))
    # Login
    if choice1 == "login" or choice1 == "Login" or choice1 == "LOGIN":
        start_stopper = 1
        login()
    # Sign up
    elif choice1 == "signup" or choice1 == "Signup" or choice1 == "sign up" or choice1 == "Sign up":
        start_stopper = 1
        signup()
        choice3 = str(input("Would you like to login now(yes/no)?: "))
        if choice3 == "yes" or choice3 == "Yes" or choice3 == "YES":
            login()
        else:
            print("Bye! See you soon")
    elif choice1 == "exit" or choice1 == "EXIT" or  choice1 == "Exit":
        print("Bye! See you soon")
        break