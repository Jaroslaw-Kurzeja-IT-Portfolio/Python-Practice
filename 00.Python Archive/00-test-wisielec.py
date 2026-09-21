######### Inicjalizacja

slowo = "kanapa"

haslo = []
for _ in range(len(slowo)):
    haslo.append("_")

######### Funkcje



######### Główna część programu

print("".join(haslo))

while True:

    litera = input("Podaj literę: ")

    lista_indeksow_w_slowie = []
    x = 0
    for i in slowo:
        if i == litera:
            lista_indeksow_w_slowie.append(x)
        x += 1

    print(lista_indeksow_w_slowie)

    for j in lista_indeksow_w_slowie:
        haslo[j] = litera


    print("".join(haslo))
