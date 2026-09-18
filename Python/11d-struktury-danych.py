# dictionary - słownik

# zainicjalizowany pusty słownik
countries_and_capitals = {}

# zainicjalizowany słownika z elementami
countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}

# dodanie elementu do słownika / w ten sam sposób można podmienić wartość dla już istniejącego klucza
countries_and_capitals["Czechia"] = "Prague"

print(countries_and_capitals)

# wyświetlenie wszystkich kluczy słownika
for key in countries_and_capitals.keys():
    print(key)

# wyświetlenie wszystkich wartości słownika
for value in countries_and_capitals.values():
    print(value)

# wyświetlenie wszystkich kluczy i wartości słownika
for key, value in countries_and_capitals.items():
    print(key + " - " + value)

# wyświetlenie wartości z podanego klucza - jeżeli nie ma takiego klucza, to zwraca błąd
print(countries_and_capitals["Poland"])

# wyświetlenie wartości z podanego klucza - jeżeli nie ma takiego klucza, to zwraca "None"
print(countries_and_capitals.get("Poland"))
print(countries_and_capitals.get("USA"))

# metoda ta służy do dodania nowego klucza i wyświetlenia jego wartości:
# gdy nie było tego klucza to dodaje nowy klucz i wartość do słownika, a potem wyświetla tą nową wartość
# gdy był już taki klucz, to nic nie zamienia, tylko wyświetla starą wartość tego klucza
print(countries_and_capitals.setdefault("USA", "Washington DC"))
print(countries_and_capitals)


# usuwanie elementu ze słownika / do tego zwraca wartość usuniętego klucza
# gdy go nie było, to wyświetla stringa po przecinku
print(countries_and_capitals.pop("RPA", "nie ma"))
print(countries_and_capitals)

# usuwanie ostatnio dodaną wartość do słownika / do tego zwraca ten właśnie usunięty element w formie tuple (krotki)
print(countries_and_capitals.popitem())
print(countries_and_capitals)

# sprawdzenie czy klucz znajduje się w słowniku / akcja jeżeli klucz jest/nie jest w słowniku
country = input("Szukaj państwa: ")

if country.capitalize() in countries_and_capitals:
    print("znaleziono")
else:
    print("nie znaleziono")

# usunięcie wszystkich elementów słownika
print(countries_and_capitals.clear())