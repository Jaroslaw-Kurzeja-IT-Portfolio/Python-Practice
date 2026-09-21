plik = open("abc.txt", "w+") # użyta funkcja do otwarcia połączenia z plikiem

alfabet = {"a": "1", "b": "2", "c": "3"}

for litery, liczby in alfabet.items():
    plik.write(litery + " - " + liczby + "\n") # użyta metoda do nadpisania w otwartym połączeniu z plikiem

plik.close() # użyta metoda do zamknięcia połączenia

###

def load_tasks_from_file(): # funkcja wczytująca dane z pliku
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

###

def delete_task():
    task_index = int(input("Podaj indeks zadania do usunięcia: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("Zadanie o tym indeksie nie istnieje.")
        return
    
    tasks.pop(task_index)
    print("Usunięto zadanie!")


# wczytywanie z pliku:
#   - otworzenie połączenia za pomocą funkcji (z przypisaniem do zmiennej)
#   - odczytanie przy pomocy pętli for:
#       for line in file.readlines(): <--- iteruje linie z obiektu liń pliku
#           instrukcje: tasks.append(line.strip()) <--- dodaje zadania z pobranej linijki pliku przy pomocy metody .strip()
#   - zamknięcie połączenia 
# zapisanie do pliku:
#   - otworzenie połączenia za pomocą funkcji (z przypisaniem do zmiennej)
#   - zapisanie przy pomocy pętli for:
#       for task in tasks: <--- iteruje zadania z listy zadań
#           instrukcje: file.write(task + "\n") <--- zapisuje zadanie przy pomocy metody .write()
#   - zamknięcie połączenia przy pomocy metody "zmienna.close()"

# -----------------------------------------------
# Zobaczyć jak to wszystko działa:
# -
# -
# -
# -----------------------------------------------

# zapoznać się z dokumentacją; zobaczyć jakiego rodzaju tryby (np. r, w, w+) mamy, co możemy z plikami zrobić, w jaki sposób
# je otwierami, gdzie ustawiony jest kursor
