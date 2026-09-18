name = "kAmil"

print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name[2])
print(name[1:2])
print(name[3:])
print(name[-3:-1])

# "metody - to takie funkcje, które przypisane są do danego obiektu"
# "metody, podobnie jak funkcje, mogą przyjmować argumenty" argumenty są podawane w nawiasach okrągłych w funkcji

# name[x:y] zwraca litery ze zmniennej string czytane od lewej do prawej
# x - pozycja (indeks litery) od której ma zacznąć:
# gdy podawana od lewej - wartość liczona od 0
# gdy podawana od prawej - wartość liczona od -1
# y - pozycja (indeks litery) do której skończy (ale bez niej)


channel = "Jak nauczyć się programowania"

print(channel.split(" "))
# metoda do rozdzielenia sprinta (w tym przypadku spacją tj. " ")
# tworzt się lista z poszczególnymi słowami tego stringa

join_string = " "
print(join_string.join(["Jak", 'nauczyć', 'się', 'programowania']))
# metoda do łączenia z listy słów

print(name.startswith("k"))
print(name.startswith("K"))
# metoda która sprawdza czy string zaczyna się znakiem

print(name.endswith("a"))
print(name.endswith("l"))
# metoda która sprawdza czy string kończy się znakiem

print(name.rstrip("l"))
# metoda która usuwa znak z prawej strony stringa

print(name.lstrip("k"))
# metoda która usuwa znak z lewej strony stringa

print(name.strip("l"))
# metoda która usuwa znak po obu stronach stringa

print(name.strip())
# metoda która usuwa nadmierne spacje i znaki nowej linii po obu stronach stringa

first_name = "Kamil"
second_name = "Brzeziński"

print(first_name + " " + second_name)
# łączenie stringów "na piechotę"

join_string = " "
print(join_string.join([first_name, second_name]))
# łączenie stringów przy pomocy metody join

james_bond = 7
print(str(james_bond).zfill(3))
# wyświetlenie zamienionego int na str i uzupełnienie odpowiednią ilością zer



