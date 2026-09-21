# 1:49:45

user_choice = 0

tasks = []


def show_tasks():
    print("Lista TO DO:")
    task_index = 0
    for task in tasks:
        print("[" + str(task_index + 1) + "] " + task)
        task_index += 1

def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano zadanie!")

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

def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()
    print("Zapisano zadania!")

def load_tasks_from_file():
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

def show_user_choice_list():
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")

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

load_tasks_from_file()

while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    elif user_choice == 2:
        add_task()

    elif user_choice == 3:
        delete_task()

    elif user_choice == 4:
        save_tasks_to_file()

    elif user_choice == 0:
        show_user_choice_list()

    else:
        print("Brak takiej możliwości. Wybierz liczbę z Menu.")

    user_choice = show_choose_number()