# 1:49:45

user_choice = 0

tasks = []


def show_tasks():
    print("Lista TO DO:")
    task_index = 0
    for task in tasks:
        print("[" + str(task_index + 1) + "] " + str(task))
        task_index += 1

def add_task():
    task = []
    task_name = input("Wpisz treść zadania: ")
    task.append(task_name)
    task_class = input("Podaj kategorię zadania: ")
    task.append(task_class)
    task_status = input("Podaj status zadania: ")
    task.append(task_status)
    tasks.append(task)
    print("Dodano zadanie!")

# def add_task_class():
#     .

# def a add_task_status():
#     .

# def add_task():
#     .

def delete_task():
    try:
        task_index = int(input("Podaj indeks zadania do usunięcia: ")) - 1
    except ValueError:
        print("Niepoprawny wybór.")
        return

    if task_index < 0 or task_index > len(tasks) - 1:
        print("Zadanie o tym indeksie nie istnieje.")
        return

    tasks.pop(task_index)
    print("Usunięto zadanie!")

def save_tasks_to_file(file_name):
    if the_list_has_file_already:
        print()
    else:
        file_name = str(input("Podaj nazwę pliku do zapisu:") + ".txt")
    file = open(file_name, "w")
    # file = open("file.txt", "w")
    for task in tasks:
        file.write(str(task) + "\n")
        print(str(task) + "\n")
    file.close()
    print("Zapisano zadania!")
    return the_list_has_file_already, file_name

def load_tasks_from_file():
    if someth_is_changed_in_current_file:
        want_to_save = int(input("Czy chcesz zapisać zmiany do pliku przed otworzeniem innej listy? [1] Tak / Nie [2] ):"))
        if want_to_save == 1:
          save_tasks_to_file()  
    file_name = str(input("Podaj nazwę pliku, z którego otworzyć listę TO DO: ")) + ".txt"
    the_list_has_file_already = True
    try:
        file = open(file_name)

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return the_list_has_file_already, file_name
    return the_list_has_file_already, file_name

# [0]
def show_main_menu():
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Edytuj zadanie")
    print("4. Usuń zadanie")
    print("5. Edytuj kategorię")
    print("6. Zapisz (aktualną listę)")
    print("7. Zapisz jako...")
    print("8. Otwórz listę")
    print("9. Wyjdź z programu")

# [1] show_tasks_menu
# [2] ---- (dodaj zadanie)
# [3] show_edit_task
def show_edit_task_menu():
    print("1. Zmień kategorię zadania")
    print("2. Zmień status zadania")
    print("3. Wróć do Menu głównego")
# Podaj numer zadania, którego kategorię chcesz zmienić:
# wyświetla listę kategorii
# Wybierz kategorię dla tego zadania:

# Podaj numer zadania, którego status chcesz zmienić:
# wyświetla listę statusó: do zrobienia / w trakcie wykonywania / zrobione
# Wybierz status dla tego zadania:

# [4] ----- (usuń zadanie)
# [5] show_class_menu
def show_class_menu():
    print("1. Dodaj kategorię")
    print("2. Zmień nazwę kategorii")
    print("3. Usuń kategorię")
    print("4. Wróć do Menu głównego")
# dalsze wybory nie potrzebują (pod)menu


def show_choose_number():
    print("======================================")
    print('(Aby wyświetlić Menu - wybierz "0")')
    try:
        user_choice = int(input("Wybierz liczbę: "))
    except ValueError:
        print("Niepoprawny wybór.")
        user_choice = -1
    print("--------------------------------------")    
    return user_choice

someth_is_changed_in_current_file = False

zwrot_z_funkcji_load = load_tasks_from_file()
the_list_has_file_already = zwrot_z_funkcji_load[0]
file_name = zwrot_z_funkcji_load[1]
print(the_list_has_file_already)
print(file_name)

while user_choice != 9:
    if user_choice == 1:
        show_tasks()

    elif user_choice == 2:
        add_task()

    elif user_choice == 3:
        show_edit_task_menu()

    elif user_choice == 4:
        delete_task()

    elif user_choice == 5:
        show_class_menu()

    elif user_choice == 6:
        zwrot_z_funkcji_save = save_tasks_to_file(file_name)
        the_list_has_file_already = zwrot_z_funkcji_save[0]
        file_name = zwrot_z_funkcji_save[1]

    elif user_choice == 7:
        the_list_has_file_already = False
        zwrot_z_funkcji_save = save_tasks_to_file(file_name)
        the_list_has_file_already = zwrot_z_funkcji_save[0]
        file_name = zwrot_z_funkcji_save[1]

    elif user_choice == 8:
        tasks = []
        zwrot_z_funkcji_load = load_tasks_from_file()
        the_list_has_file_already = zwrot_z_funkcji_load[0]
        file_name = zwrot_z_funkcji_load[1]
        
    elif user_choice == 0:
        show_main_menu()
    else:
        print("Brak takiej możliwości. Wybierz liczbę z Menu.")

    user_choice = show_choose_number()