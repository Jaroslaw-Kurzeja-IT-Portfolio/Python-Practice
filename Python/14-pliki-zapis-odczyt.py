#1:43:40
# zapoznać się z dokumentacją; zobaczyć jakiego rodzaju tryby (np. r, w, w+) mamy, co możemy z plikami zrobić, w jaki sposób
# je otwierami, gdzie ustawiony jest kursor


# argument "r" jest domyślny i oznacza tylko do odczytu; argument "w+" oznacza do zapisu i odczytu
file = open("countries_and_capitals.txt", "w+")

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin", "Czechia": "Prague"}

for country, capital in countries_and_capitals.items():
    file.write(country + " - " + capital + "\n")

file.close()

###

file = open("countries_and_capitals.txt")

for line in file.readlines():
    print(line.strip())

# metoda .strip() usuwa znaki końca linii oraz spacje(?)

file.close()
