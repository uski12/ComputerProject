import math

usernames = {
    "Kathir": ["mental05", 1399, "+91 77608 99599"],
    "Sidharth": ["beartreiten69", 2599, "+91 97390 47252"],
    "Samved": ["sam420", 1999, "+91 90084 90106"],
    }


def ask_username():
    return input("\nEnter your username: ")


def ask_password():
    return input("Enter your password: ")


def sign_up():
    while True:
        name = ask_username()
        if(name in usernames.keys()):
            print("Username already exists! Try again")
            continue
        else:
            usernames[name] = [0, 0, 0]
            usernames[name][0] = ask_password()
            usernames[name][2] = input("Enter your phone number: ")
            print("Account created successfully!")
            break


def log_in():
    while True:
        usr = ask_username()
        if usr in usernames.keys():
            if ask_password() == usernames[usr][0]:
                print("Successfully logged in.")
                display(usr)
        if input("Wrong username or password. Enter 2 to try again, or any other number to exit to main menu: ") == "2":
            continue
        else:
            break


def display(usr):
    print("\n--------------Account Details--------------\n")
    print("Username: '", usr, "'\t|\tBalance: INR ", usernames[usr][1], "\t|\tContact Number: ", usernames[usr][2], sep="")
    update_balance(usr)


def transfer(usr, recipient):
    while True:
        money = math.fabs(int(input("Enter how much you want to transfer: ")))
        if usernames[usr][1] < money:
            print("ERROR: Insufficient balance.")
            continue
        else:
            usernames[usr][1] -= money
            usernames[recipient][1] += money
            print("Transaction successful!")
            display(usr)
            break


def update_balance(usr):
    print("\nEnter:\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Exit")
    choice = input("Enter 1/2/3/4: ")
    if choice == "1":
        amount = math.fabs(int(input("Enter how much you want to deposit: ")))
        usernames[usr][1] += amount
        print("\nAmount deposited successfully.")
    elif choice == "2":
        amount = math.fabs(int(input("Enter how much you want to withdraw: ")))
        if amount <= usernames[usr][1]:
            usernames[usr][1] -= amount
            print("\nINR", amount, "withdrawn successfully.")
        else:
            print("You don't have enough balance.")
    elif choice == "3":
        recipient = input("\nEnter a user to transfer funds to: ")
        if recipient in usernames.keys():
            transfer(usr, recipient)
        else:
            print("Recipient does not exist.")
    elif choice == "4":
        exit(1)
    display(usr)


print("\t\t\t\tWelcome to the Bank Portal!\n\t\t\t\t\tMain Menu")
while True:
    print("\n-----------------------------------------------------\nEnter:\n1. Create a new account\n2. Log in to an "
          "existing account\n3. Exit")
    choice = input("Enter 1/2/3: ")
    if choice == "1":
        sign_up()
        choice = input("\nEnter 2 to log in to an existing account, 3 to exit: ")
    if choice == "2":
        log_in()
    if choice == "3":
        exit(1)
