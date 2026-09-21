# lista (elementów) służy do grupowania elementów zwykle tego samego typu (ale nie muszą być tego samego typu)
#   poniżej:
#       - zainizjalizowanie listy 
#       - dodawanie i odejmowanie elementu do/z listy
#       - sortowanie listy, odwrotne sortowanie listy, odwracanie kolejności listy
#       - wyświetlanie kolejnych elementów listy, wyświetlenie danego elementu listy
#       - podanie ilości elementów listy, podanie ile razy występuje dany element na liście
#       - wyświetlenie danego elementu listy z jego usuwaniem
#       - usuwanie wszystkich elementów listy
#       - łączenie kilku list

# zainicjalizowanie pustej listy
names_list = []
# metoda do dodawania elementów do listy
names_list.append("Kamil")
names_list.append("Mariusz")

print(names_list)

# zainicjalizowanie listy i dodanie od razu elementamów
names_list2 = ["Kamil", "Mariusz", "Adam"]
print("\nLista nr 2: " + str(names_list2))

# posortowanie elementów w liście alfabatycznie
names_list2.sort()

print("\nLista nr 2 po posortowaniu: " + str(names_list2))

# posortowanie elementów w liście alfabetycznie od tyłu
names_list2.sort(reverse=True)

print("\nLista nr 2 po posortowaniu odwrotnym: " + str(names_list2))

# odwrócenie listy
names_list2.reverse()

print("\nLista nr 2 po odwróceniu jej: " + str(names_list2))

# wyświetlenie kolejnych elementów listy
print("\nwyświetlenie kolejnych elementów listy nr 2:")
for name in names_list2:
    print(name)

print(type(name))

names_list3 = ["Kamil", "Mariusz", "Adam", "Kamil"]

# metoda służąca do podania długości listy (ile elementów zawiera)
print(len(names_list3))

# metoda służąca do podania ile razy dany element występuje na liście
print(names_list3.count("Kamil"))
print(names_list3.count("Mariusz"))
print(names_list3.count("Jarek"))

print(names_list3)

# wyświetlenie konkretnego elementu listy - wartość elementu zostanie tylko zwrócona
print(names_list3[0])

print(names_list3)

# wyświetlenie konkretnego elementu listy - ta metoda zwraca wartość elementu i zostaje on usunięty z listy
print(names_list3.pop(0))

print(names_list3)

names_list3.append("Mariusz")
print(names_list3)

# metoda usuwa element bez zwracania jego wartości (usuwa pierwsze element w kolejności o podanej wartości)
names_list3.remove("Mariusz")

print(names_list3)

# metoda usuwa wszystkie elementy z listy
names_list3.clear()

print(names_list3)

# łączenie list
names_list4 = names_list + names_list2
print(names_list4)

# łączenie elementów listy w jednego stringa / znak lub znaki łączące w cudzysłowiu ""
print("-".join(names_list4))
print(type("-".join(names_list4)))