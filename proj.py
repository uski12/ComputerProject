

usernames = {
    "anshul": 0,
    "sid": 1,
    "samved": 2
    }
details = [["ansh", 50],["si", 100], ["sam", 500]]


def ask_username():
    return input("\nEnter your username: ")


def ask_password():
    return input("\nEnter your password: ")


def sign_up():
    usernames[ask_username()] = len(details)
    details.append([ask_password(), 0])
    print("\nAccount created successfully!")


def log_in():
    while True:
        usr = ask_username()
        try:
            indx = usernames[usr]
            if (ask_password() == details[indx][0]):
                print("\nSuccessfully logged in.")
                display(usr)
        except:
            input("Username not found. Enter 1 to try again, or any other number to exit to the main menu: ")
            if(input=="1"):
                continue
            else:
                break


def display(usr):
    print("\n--------------Account Details--------------\n")
    print("Username: '", usr, "'\t|\tBalance: INR ", details[usernames[usr]][1], sep="")
    update_balance(usr)


def transfer(usr, recipient):
    indx = usernames[usr]
    rcpIndx = usernames[recipient]
    while True:
        money = int(input("\nEnter how much you want to transfer: "))
        if(money>details[indx][1]):
            print("Insufficient balance.")
            continue
        else:
            details[indx][1] -= money
            details[rcpIndx][1] += money
            print("Transaction successful. ")
            display(usr)
            break
    details[rcpIndx][1] #recipient's balance


def update_balance(usr):
    print("\nEnter:\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Exit")
    choice = input("Enter 1/2/3/4: ")
    if choice == "1":
        details[usernames[usr]][1] += int(input("Enter how much you want to deposit: "))
        print("\nAmount deposited successfully.")
    elif choice == "2":
        amount = int(input("Enter how much you want to withdraw: "))
        if details[usernames[usr]][1] >= amount:
            details[usernames[usr]][1] -= amount
            print("\nINR", amount, "withdrawn successfully.")
        else:
            print("You don't have enough balance.")
    elif choice == "3":
        recipient = input("\nEnter a user to transfer funds to: ")
        transfer(usr, recipient)
    elif choice == "4":
        exit(1)
    display(usr)



print("\t\t\t\tWelcome to the Bank Portal!\n\t\t\t\t\tMain Menu")
while True:
    print("\n-----------------------------------------------------\nEnter:\n1. Create a new account\n2. Log in to an existing account\n3. Exit")
    choice = input("Enter 1/2/3: ")
    if choice == "1":
        sign_up()
        choice = input("\nEnter 2 to log in to an existing account, 3 to exit: ")
    if choice == "2":
        log_in()
    if choice == "3":
        exit(1)
