import time

def signup():
    get_saved_user_name()
    asking_for_username()

def signup1():
    get_saved_pass_word()
    asking_for_password()

def get_saved_user_name():
    filename = 'username.txt'
    name = None
    try:
        with open(filename, 'r') as inf:
            return inf.read()
    except FileNotFoundError:
        pass

    name = input("Please enter a username: ")
    with open(filename, 'w') as outf:
        outf.write(name)
    return name

def get_saved_pass_word():

    filename = 'password.txt'
    name = None
    try:
        with open(filename, 'r') as inf:
            return inf.read()
    except FileNotFoundError:
        pass

    name = input("Please enter a secure password: ")
    with open(filename, 'w') as outf:
        outf.write(name)
    return name
    signup1()

def asking_for_username():
    question1 = input("Is this the username you would like to use? YES/NO : ")
    if question1 == "YES":
        signup1()
    if question1 == "NO":
        import os
        os.remove("username.txt")
        signup()

def asking_for_password():
    question2 = input("Is the password you would like to use? YES/NO : ")
    if question2 == "YES":
        print("good")
    if question2 == "NO":
        import os
        os.remove("password.txt")
        signup1()

def login():
    print("Welcome to Pady's secure login system!")
    time.sleep(2)
    sign_up = input("Have you already signed up? YES/NO : ")
    if sign_up == "NO":
        signup()
    if sign_up == "YES":
        print("NICE!")
    else:
        print("This is not a valid answer please try again.")
        time.sleep(2)
        login()
    
login()