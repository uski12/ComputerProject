import math
import mysql.connector as con

#Connect to database
link = con.connect(host = "localhost", user="root", passwd = "2919119", database = "bank")
if link.is_connected():
    print("Connected to database.")

#DATABASE STRUCTURE = ('username', 'phone number', 'email', balance, 'password')

cursor = link.cursor()
cursor.execute("select usrname from data;")
usr_list = cursor.fetchall() #Retrieve username data from database


def ask_username():
    return input("\nEnter your username: ")


def ask_password():
    return input("Enter your password: ")

#
def sign_up():
    while True:
        name = ask_username()
        if(name,) in usr_list:
            print("Username already exists! Try again")
            continue
        else:
            ph_no = input("Enter your phone number: ")
            email = input("Enter your email: ")
            passwd = ask_password()
            cursor.execute("insert into data values('{}', '{}', '{}', {}, '{}');".format(name, ph_no, email, 0, passwd))
            link.commit()
            print("Account created successfully!")
            break


def log_in():
    while True:
        user = ask_username()
        if (user, ) in usr_list:
            cursor.execute("select passwd from data where usrname='{}';".format(user,))
            pwl = cursor.fetchall()
            if (ask_password(),) in pwl:
                print("Successfully logged in.")
                display(user)
        if input("Wrong username or password. Try again? (y/n) ") in "yY":
            continue
        else:
            break


def display(user):
    cursor.execute("select * from data where usrname='{}';".format(user))
    data = cursor.fetchone()
    print("\n--------------Account Details--------------\n")
    print("Username: '", data[0], "'\t|\tBalance: INR ", data[3], "\t|\tContact Number: ", data[1],"\t|\tE-mail: ", data[2], sep="")
    update_balance(user, data[3])


def update_balance(user, bal):
    print("\nEnter:\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Exit")
    choice = input("Enter 1/2/3/4: ")
    if choice == "1":
        amount = math.fabs(float(input("Enter how much you want to deposit: ")))
        cursor.execute("update data set balance={} where usrname='{}';".format(bal+amount, user))
        print("\nINR", amount, "deposited successfully.")
    elif choice == "2":
        amount = math.fabs(float(input("Enter how much you want to withdraw: ")))
        if amount <= bal:
            cursor.execute("update data set balance={} where usrname='{}';".format(bal-amount, user))
            print("\nINR", amount, "withdrawn successfully.")
        else:
            print("ERROR: You do not have enough balance.")
    elif choice == "3":
        recipient = input("\nEnter a user to transfer funds to: ")
        if (recipient,) in usr_list:
            transfer(user, recipient, bal)
        else:
            print("ERROR: Recipient does not exist.")
    elif choice == "4":
        exit(1)
    link.commit()
    display(user)


def transfer(user, recipient, bal):
    amount = math.fabs(float(input("Enter how much you want to transfer: ")))
    if bal >= amount:
        cursor.execute("update data set balance={} where usrname='{}';".format(bal - amount, user))
        cursor.execute("select balance from data where usrname='{}';".format(recipient))
        rec_bal = cursor.fetchone()
        cursor.execute("update data set balance={} where usrname='{}';".format(rec_bal[0] + amount, recipient))
        print("Transaction successful!")
    else:
        print("ERROR: Insufficient balance.")



print("\t\t\t\tWelcome to the Bank Portal!\n\t\t\t\t\t\tMain Menu")
while True:
    print("\n","-"*53,"\nEnter:\n1. Create a new account\n2. Log in to an existing account\n3. Exit")
    choice = input("Enter 1/2/3: ")
    if choice == "1":
        sign_up()
        choice = input("\nEnter 2 to log in to an existing account, 3 to exit: ")
    if choice == "2":
        cursor.execute("select usrname from data;")
        usr_list = cursor.fetchall()
        log_in()
    if choice == "3":
        exit(1)