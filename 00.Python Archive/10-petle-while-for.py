number = 1

# pętla while będzie się wyświetlac i powtarzać tak długo jak zwrócona jej wartość będzie true 
print("Poniżej pętla while:")
while number < 6:
# powyżej może być dowolne wyrażenie zwracającą wartość bool
    print(number)
    number += 1


# pętla for będzie się powtarzać określoną ilość razy

# zakres od lewej strony jest zakresem domkniętym,
# a od prawej - otwartym (czyli jak dojdzie do tej wartości, to przestanie się wyświetlać)

print("Poniżej pętla for z zakresem (1, 6):")
for number in range(1, 6):
    print(number)

# trzeci argument to krok (o ile elementów ma liczyć)
print("Poniżej pętla for z zakresem (0, 10, 2):")
for number in range(0, 10, 2):
    print(number)

# instrukcja break i continue jest dostępna dla oby typów pętli, czyli zarówno dla while jak i for 
# instrukcja break - przerywa wywołanie pętli, gdy osiągnięta jest wartość
print("Poniżej instrukcja break (dla wartości 5):")
for number in range(0, 10):
    if number == 5:
        break
    print(number)

# instrukcja continue - przerywa aktualne wywołanie pętli dla podanej wartości i kontynuuje od kolejnego wywołania pętli
print("Poniżej instrukcja continue (dla wartości 5):")
for number in range(0, 10):
    if number == 5:
        continue
    print(number)