## 1. Wybór niedostępnej opcji (tzn. wybierze liczbę z poza dostępnych)
#   Rozwiązanie:
#       Sposób: dla wartość integer innych jak z menu ---> if; dla innych wartości jak integer ---> ValueError
#       Miejsce w kodzie: przy wyborze opcji z menu; przy opcji kasowania zadania
# 2. Zaienić listę na: set, dictionaty (trzeba pomyśleć w jaki sposób decydować o kluczach... patrz: filmik)
# 3. Pobranie nazwy pliku od użykownika (z jakiego ma być wczytywana ta lista 'to do')
# 4. Status zadań: do wykonania, które wykonujemy, wykonane
#       Sposób: podobnie jak "kategorie"
# 5. Zmiana formatu zapisywanych zadań (możnaby wykorzystać format Json)
# 6. Podział zadań na różne kategorie (np. powiązane z domem, z pracą, z rozrywką, z nauką itd.)
#     wpisanie zadania >> nadanie kategorii z pomocą indeksu (0 - dla dodanie nowej kategorii)
# 7. Automatyczne zapisywanie listy zadań przy wyjściu
#           Pyta przy wyjściu:
#           A.jeżeli jeszcze ich nie zapisał:
#                "Zapisz i wyjdź" (1. zapisuje w domyślnym pliku 2. nie ma jeszcze domyślnego pliku, trzeba go wybrać)
#                "Nie zapisuj i wyjdź" "Wróć"
#           B.nie pyta, bo nie było zmian od ostatniego zapisania i po prostu zamyka.
#
#
# 8. Schowana lista możliwości / wyświetl listę możliwości (show_user_choice_list) po naciśnięciu "0"
#       Sposób: stworzenie funkcji zawierające wyświetlenie Menu; dodanie instrukcji warunkowej dla wartości 0
#               z odwołaniem do funkcji z Menu; początkowa wartość 0, żeby na początku korzystania już wyświetliło Menu 
# 9. Numery zadań na liście zaczynają sie od 1 (już nie od 0)
#       Sposób: przy usuwaniu zadań wartość zmniejszona o 1; przy wyświetlaniu wartość zwiększona o 1
# 10. Edytuj kategorie: [1] dodaj kategorię / [2] zmień nazwę kategorii / [3] usuń kategorię / [0] wróć
#       Sposób: zadanie zmienić ze str na list, aby można było edytować kategorię
#               stworzenie funkcji z wyświetleniem podmenu
#               stworzenie funkcji z pętlą while i instrukcjami warunkowymi dla wartości int 0-3
#               stworzenie funkcji dla dodania kategorii
#               stworzenie funkcji dla zmiany nazwy kategorii
#               stworzenie funkcji dla usunięcia kategorii "czy na pewno chcesz usunąć tą kategorię? będzie się to wiązało z usunięciem jej z przypisanego zadania"
#               poprawić zapis i odczyt z pliku w związku z listą i elementem kategorii
# 11. "Zapisz" i "zapisz jako..."
#
#
#
# A. zaznaczenie, że jak doszło do zmiany, to 
#
#
#
#
# B. zaznaczenie, że do aktualnej TO DO listy jest przypisany plik do zapisu. kiedy:
#       - zaraz po uruchomieniu (albo już istnieje i zostanie wczytany, albo nie istnieje i stworzony zostanie przy zapisie)
#       - przypisany zostanie po użyciu "zapisz jako..."
#       - przypisany zostanie po użyciu "otwórz (z pliku)"
#
#
#
