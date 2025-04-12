User = input("What is your Name >> " )

def add():
    user_name = input("Account Name >>")
    password = input("Account Password >>")

    with open("password.txt", "a") as file:
        file.write(user_name + "|" + password + "\n")


def view():
    with  open("password.txt", "r" ) as file:
        for line in file.readlines():
            data = line.strip()
            user , passw = data.split("|")
            print(f"Username: {user}, Password: {passw}")


while True:
    mode = input("Do you want to add or view password (view/add) or quit >> ").lower()
    if mode == "quit":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else :
        print("Invalid input")
        continue