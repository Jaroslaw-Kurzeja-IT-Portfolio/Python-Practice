# Zmiana wersji v.0.1 na wesję v.0.2:

#   - WERSJA v.0.1 implementuje walidację wyboru w main menu i obsługę wyboru sekwencyjnie.
#     (przepływ: validate_choice() --> handle_menu_choice() )

#   - WERSJA v.0.2 wprowadza rozdzielenie odpowiedzialności w powyższym zakresie.
#     (validate_choice(), handle_menu_choice() )


# Imports


# Variables and Constants


username = ""
password = ""
login_username = ""
login_password = ""
choice = ""
running = True
session_running = True
users = []
login_successful = False

# Function Definitions

def main_menu(): 
    print("LOGIN SYSTEM")
    print("1. Register")
    print("2. Login")
    print("3. Exit")


def user_menu():
    print("LOGIN SYSTEM")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Logout")
    print("4. Log-out and Exit")


def get_choice():
    choice = input("Choose an option: ")
    return choice


def validate_choice(choice):
    running = True
    if choice not in ["1", "2", "3"]:
        print()
        print("Invalid choice. Please select an option from 1 to 3.")
        print()
    else:
        running = handle_menu_choice(choice)
    return running


def register():
    print()
    print("REGISTER")
    file = open("users.txt", "w+")
    username = input("Enter username: ")
    password = input("Enter password: ")
    file.write(username + ":" + password + "\n")
    file.close()


def login():
    print()
    print("LOGIN PROCCESS")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    return login_username, login_password


def check_login(login_username, login_password):
    login_successful = False
    users = load_users()
        
    for user in users:
        username, password = user.split(":")
        
        if (login_username == username and login_password == password):
            login_successful = True
            break
        else:
            login_successful = False

    if login_successful == True:
        print("Login successful!")
    else:
        print("Invalid username or password.")
    return login_successful


def load_users():
    file = open("users.txt", "r")
    users = file.read().strip().split("\n")
    file.close()
    return users


def handle_menu_choice(choice):
    if choice == "1":
        register()

    elif choice == "2":
        login_username, login_password = login()
        login_successful = check_login(login_username, login_password)
        if login_successful:
            return user_session()


    elif choice == "3":
        print("Goodbye")
        return False
    return True


def user_session():

    while session_running:
        user_menu()
        choice = get_choice()

        if choice == "1":
            print("aaaaaa")
        elif choice == "2":
            print("bbbbbb")
        elif choice == "3":
            print("Goodbye")
            return True
        elif choice == "4":
            print("Goodbye")
            return False
            

        
# Main Program / Main Logic


while running:
    main_menu()
    
    choice = get_choice()

    running = validate_choice(choice)


    # running = handle_menu_choice(choice)
