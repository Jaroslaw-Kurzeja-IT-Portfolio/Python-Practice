
# pusty zbiór (set)
names_set = set()

# deklarowanie wartości w zbiorze
names_set = {"Kamil", "Mariusz", "Kamil"}

# elementy nie mogą się duplikować, dlatego tu tylko 2 elementy
print("1. " + str(names_set))

# metoda dodająca element do zbioru
names_set.add("Jurek")
names_set.add("Zbyszek")
names_set.add("Maksymilian")

print("\n2. " + str(names_set))

# dwie metody usuwające element ze zbioru
# różnica jest taka, że w remove jak element, który chcemy usunąć, nie istnieje, zwróci błąd
# a w discard nie zrobi nic, bo element nie istniał, ale też nie zwróci błędu
names_set.remove("Kamil")
names_set.discard("Kamil")

print("\n3. " + str(names_set))

# nie da się dołączyć listy, ale można krotkę
names_tuple = ("hallo", "cześć")
names_set.add(names_tuple)

print("\n4. " + str(names_set))

# łączenie setów (nie da się plusem "+")
names_set2 = {"Ola", "Jola", "Marta"}
names_set3 = names_set.union(names_set2)

print("\n5. " + str(names_set3))

# metoda do powiększenia zbioru o inny
names_set.update(names_set2)

print("\n6. " + str(names_set))

# odejmowanie zbioru o wartości z innego (porównywanie zbiorów)
names_set = names_set3.difference(names_set2)

print("\n7. " + str(names_set))

# metoda szuka części wspólnych dwóch zbiorów
print("\n8. " + str(names_set3.intersection(names_set2)))

# metoda szuka części NIEwspólnych dwóch zbiorów
print("\n9. " + str(names_set3.symmetric_difference(names_set2)))

# metoda usuwa wszystkie jego elementy
print("\n10. " + str(names_set.clear()))

# powiększenie listy o zbiór - dodawanie zbioru do listy
names_list = ["duży", "mały"]
print(names_list)
print(names_set3)
print("\n11. " + str(names_list.extend(names_set3)))
print(names_list.extend(names_set3))


