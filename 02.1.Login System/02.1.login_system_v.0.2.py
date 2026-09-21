# Zmiana wersji v.0.1 na wesję v.0.2:

#   - WERSJA v.0.1 implementuje walidację wyboru w main menu i obsługę wyboru sekwencyjnie.
#     (przepływ: validate_choice() --> handle_main_menu_choice() )

#   - WERSJA v.0.2 wprowadza rozdzielenie odpowiedzialności w powyższym zakresie.
#     (validate_choice(), handle_main_menu_choice() )



#### Imports


#### Variables and Constants


username = ""
password = ""
login_username = ""
login_password = ""
choice = ""
program_running = True
session_running = True
users = []
login_successful = False


#### Function Definitions


### Main Menu - Main Part

def main_menu():
    print()
    print("LOGIN SYSTEM")
    print("1. Register")
    print("2. Login")
    print("3. Exit")


def main_menu_session(program_running):
    while program_running:
        main_menu()
    
        choice = get_choice()

        if validate_main_menu_choice(choice):
            program_running = handle_main_menu_choice(choice)


def validate_main_menu_choice(choice):
    if choice not in ["1", "2", "3"]:
        print()
        print("Invalid choice. Please select an option from 1 to 3.")
        print()
        return False
    return True


def handle_main_menu_choice(choice):
    if choice == "1":
        register()

    elif choice == "2":
        login_username, login_password = login()
        login_successful = check_login(login_username, login_password)
        if login_successful:
            return user_menu_session()

    elif choice == "3":
        print()
        print("Goodbye")
        print()
        return False
    return True

## Main menu - Choices

# 1. Register

def register():
    print()
    print("REGISTER")
    file = open("users.txt", "w+")
    username = input("Enter username: ")
    password = input("Enter password: ")
    file.write(username + ":" + password + "\n")
    file.close()


# 2. Login

def login():
    print()
    print("LOGIN PROCCESS")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    return login_username, login_password


def check_login(login_username, login_password):
    login_successful = False
    users = load_users()
        
    login_successful = find_user(users, login_username, login_password)

    if login_successful == True:
        print()
        print("Login successful!")
        print()
    else:
        print()
        print("Invalid username or password.")
    return login_successful


def load_users():
    file = open("users.txt", "r")
    users = file.read().strip().split("\n")
    file.close()
    return users


def find_user(users, login_username, login_password):
    for user in users:
        username, password = user.split(":")
        
        if (login_username == username and login_password == password):
            login_successful = True
            break
        else:
            login_successful = False
    return login_successful



### User Menu

## User Menu - Main Part

def user_menu():
    print("USER MENU")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Logout")
    print("4. Log-out and Exit")


def user_menu_session():
    session_running = True
    while session_running:
        user_menu()
        choice = get_choice()

        if validate_user_menu_choice(choice):
            program_running, session_running = handle_user_menu_choice(choice)

    return program_running


def validate_user_menu_choice(choice):
    if choice not in ["1", "2", "3", "4"]:
        print()
        print("Invalid choice. Please select an option from 1 to 4.")
        print()
        return False
    return True


def handle_user_menu_choice(choice):
    program_running = True
    session_running = True

    if choice == "1":
        print()
        print("(Option 1 - Future Content...)")
        print()

    elif choice == "2":
        print()
        print("(Option 2 - Future Content...)")
        print()

    elif choice == "3":
        print()
        print("Goodbye")
        program_running = True
        session_running = False

    elif choice == "4":
        print()
        print("Goodbye")
        print()
        program_running = False
        session_running = False

    return program_running, session_running

## User Menu - Choices

# Option 1

# Option 2


### Shared Functions

def get_choice():
    choice = input("Choose an option: ")
    return choice



#### Main Program / Main Logic:

main_menu_session(program_running)
