#nesting =  placing one block of code inside another

# exmple - login system

username = input("enter username:")
password = input("enter password:")

if username == "admin" and password == "pass":
    print("login succesfull")
else: #nesting
    if username != "admin":
        print("wrong username , try again")
    else:
        print("wrong password, try again")        