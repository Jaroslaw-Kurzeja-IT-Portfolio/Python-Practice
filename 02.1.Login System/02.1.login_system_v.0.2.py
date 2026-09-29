# Zmiana wersji v.0.1 na wesję v.0.2:

#   - WERSJA v.0.1 implementuje walidację wyboru w main menu i obsługę wyboru sekwencyjnie.
#     (przepływ: validate_choice() --> handle_main_menu_choice() )

#   - WERSJA v.0.2 wprowadza rozdzielenie odpowiedzialności w powyższym zakresie.
#     (validate_choice(), handle_main_menu_choice() )



#### Imports
import string
import keyboard
import readchar


#### Variables and Constants

allowed_username_characters = list(string.ascii_letters + string.digits + "_-!@#$%^& ")

allowed_password_characters = list(string.ascii_letters + string.digits + "_-!@#$%")

letter = ""
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
    print("=====================")
    print("LOGIN SYSTEM")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("=====================")

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
        result_login = register()

    elif choice == "2":
        login_successful = False
        result_login = login()
        if result_login != False and result_login != None:
            login_username, login_password = result_login
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
    print("=====================")
    print("REGISTER")
    print("=====================")

    register_username = get_register_username()
    if register_username is None:
        print("---------------------")
        print()
        print("Registration cancelled.")
        print()
        return

    register_password = get_register_password()
    if register_password is None:
        print("---------------------")
        print()
        print("Registration cancelled.")
        print()
        return
    
    save_user(register_username, register_password)

    print("---------------------")
    print()
    print("Registration successfull!")
    print()


def get_register_username():
    result_validation = True
    result_unique = True

    while result_validation or result_unique:
        result_validation = True
        result_unique = True

        register_username = get_input_or_cancel("Enter username: ")
        if register_username is None: return None
        
        if validate_username(register_username):
            result_validation = False
        
        if check_username_unique(register_username):
            result_unique = False

    return register_username


def get_register_password():
    result_match = True

    while result_match:
        print("---------------------")
        result_validation = True
        while result_validation:
            first_register_password = get_input_or_cancel("Enter password:  ")
            if first_register_password is None: return None
            if validate_password(first_register_password):
                result_validation = False

        print()
        second_register_password  = get_input_or_cancel("Repeat password: ")
        if second_register_password is None: return None
        if first_register_password == second_register_password:
            result_match = False
        else:
            print("---------------------")
            print()
            print("Passwords do not match. Please try again.")
            print()                
    return first_register_password


def save_user(register_username, register_password):
        file = open("02.1.Login System/users.txt", "a+")
        file.write(register_username + ":" + register_password + "\n")
        file.close()


def check_username_unique(register_username):
    users = load_users()

    for user in users:
        username, _ = user.split(":")
        if register_username == username:
            print()
            print("Username already exists. Please choose another username.")
            print()
            return False
    return True




# 2. Login

def login():
    print()
    print("=====================")
    print("LOGIN PROCCESS")
    print("=====================")

    login_username = get_input_or_cancel("Enter username: ")
    if login_username is None:
        print("---------------------")
        print()
        print("Registration cancelled.")
        print()
        return None
    if not validate_username(login_username): return False
    print("---------------------")

    login_password = get_input_or_cancel("Enter password: ")
    if login_password is None:
        print("---------------------")
        print()
        print("Registration cancelled.")
        print()
        return None
    if not validate_password(login_password): return False
    print("---------------------")


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
    file = open("02.1.Login System/users.txt", "r")
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
    print("=====================")
    print("USER MENU")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Logout")
    print("4. Log-out and Exit")
    print("=====================")


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
        print("---------------------")
        print()
        print("You have been logged out.")
        print()
        program_running = True
        session_running = False

    elif choice == "4":
        print("---------------------")
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

# readchar
def get_input_or_cancel(prompt):
    print(prompt, end="", flush=True)
    text = ""

    while True:
        key = readchar.readkey()

        if key == readchar.key.ESC:
            print()
            return None

        if key == readchar.key.ENTER:
            print()
            return text

        if key == readchar.key.BACKSPACE:
            if text:
                text = text[:-1]
                print("\b \b", end="", flush=True)
            continue

        text += key
        print(key, end="", flush=True)

# keyboard
# def get_input_or_cancel(prompt):
#     print(prompt, end = "", flush = True)
#     text = ""

#     while True:
#         event = keyboard.read_event()

#         if event.event_type != keyboard.KEY_DOWN:
#             continue

#         if event.name == "esc":
#             print()
#             return None


def get_choice():
    choice = input("Choose an option: ")
    return choice


def validate_username(username):
    invalid_length = False
    disallowed_character = False

    if username != username.strip():
        print()
        print("Space cannot be at the beginning or end of username.")
        print()
        disallowed_character = True

    if len(username) < 4:
        print()
        print("Username is too short.")
        print()
        print("---------------------")
        invalid_length = True
    elif len(username) > 20:
        print()
        print("Username is too long.")
        print()
        print("---------------------")
        invalid_length = True

    for letter in username:
        if letter not in allowed_username_characters:
            print()
            print("Username includes disallowed character(s).")
            print()
            disallowed_character = True
            break

    return not (invalid_length or disallowed_character)


def validate_password(password):
    invalid_length = False
    disallowed_character = False

    if len(password) < 8:
        print()
        print("Password is too short.")
        print()
        invalid_length = True
    elif len(password) > 20:
        print()
        print("Password is too long.")
        print()
        invalid_length = True

    for letter in password:
        if letter not in allowed_password_characters:
            print()
            print("Password includes disallowed character(s).")
            print()
            disallowed_character = True
            break

    return not (invalid_length or disallowed_character)

def show_username_rules():
    print()
    print("USERNAME RULES")
    print("Length: 4-20 characters")
    print("Allowed characters:")
    print(allowed_username_characters)


def show_password_rules():
    print()
    print("PASSWORD RULES")
    print("Length: 8-20 characters")
    print("Allowed characters:")
    print(allowed_password_characters)





#### Main Program / Main Logic:


### Test keyboard

# print("Press ESC to cancel")

# while True:
#     if keyboard.is_pressed("esc"):
#         print("ESC pressed")
#         break


### Test readchar (current version)
### Test 1: unknown, Test 2: Esc

# result = get_input_or_cancel("Test: ")

# print("Wynik:", result)
# print("Typ:", type(result))


print()
main_menu_session(program_running)

