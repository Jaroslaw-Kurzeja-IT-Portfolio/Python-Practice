file = open("abcd.txt", "w+")
# file = open("sss\\abcd.txt", "w+") # plik w folderze poniżej / użycie "\\" unika błędu jak przy \a itd.
# file = open("../zabcd.txt", "w+") # plik w folderze powyżej
# file = open("C:/Users/Jarek Dell/Desktop/nauka/zabcd.txt", "w+") # ścieżka bezwględna / przy użyciu forward slash'y
#       (jak skopiować ścieżkę dostępu pliku: trzymać SHIFT + prawy przycisk myszy (wybrać z menu))

# Tryby:
# "r" tylko do odczytu:
#       - gdy jest taki plik: ok
#       - gdy nie ma takiego pliku: FileNotFoundError: [Errno 2] No such file or directory: 'abcd.txt'
#       - metoda .read(): czyta
#       - metoda .write(): io.UnsupportedOperation: not writable
# "r+" do odczytu i zapisu

# "w" tylko do zapisu (usuwa dotychczasową treść po otwarciu połączenia):
#       - gdy jest taki plik: ok
#       - gdy nie ma takiego pliku: tworzy plik
#       - metoda .read(): io.UnsupportedOperation: not readable
#       - metoda .write(): dopisuje
# "w+" do tworzenia i zapisu (obsługuje błąd podczas odczytu, ale nie odczytuje)

# "a" tylko do zapisu (dopisując na koniec pliku):
#       - gdy jest taki plik: ok
#       - gdy nie ma takiego pliku: tworzy plik
#       - metoda .read(): io.UnsupportedOperation: not readable
#       - metoda .write(): dopisuje
# "a+" do tworzenia i zapisu (obsługuje błąd podczas odczytu, ale nie odczytuje)

# "x" do tworzenia i zapisu:
#       - gdy jest taki plik: FileExistsError: [Errno 17] File exists: 'abcd.txt'
#       - gdy nie ma takiego pliku: tworzy plik
#       - metoda .read(): io.UnsupportedOperation: not readable
#       - metoda .write(): dopisuje
# "x+" do tworzenia i zapisu (obsługuje błąd podczas odczytu, ale nie odczytuje)
# "a+" i "x+" działają identycznie

# print(type(file)) # wniosek: niezależnie od trybu (r, r+ czy a) zawsze: <class '_io.TextIOWrapper'>

print(file.read(8)) # czytanie znaków od początku pliku / argument: ilość czytanych znaków / "()" --> wszystkie znaki, "(0)" --> 0 znaków
# print(file.readline(10)) # czytanie znaków z linii / argument: ilość znak z tej linii / "()" wszystkie znaki, "(0)" 0 znaków
# print(file.readlines()) # czytanie do listy, elementami są linijki pliku /
#                         / argment: ile znaków od początku pliku zostanie wczytanych (w zaokrągleniu do końca linijki)
#                           brak argumentu ---> wszystkie znaki z pliku

file.write("jabłko\n") # dopisywanie


# file.close()
# file = open("abc.txt", "r+")

for line in file:
    print(line) # czytanie

file.write("jabłko2\n")

file.close()



