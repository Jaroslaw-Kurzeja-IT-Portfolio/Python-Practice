# for number in range(0, 10, 2):
#     print(number)

# stany początkowy
# warunek końcowy
# zmiany

# pętla ta zaczyna od wartości '0'
# będzie zwiększać wartość o '2'
# a jak dojdzie do wartości '10', to się zakończy - bez wykonywania instrukcji zawartych w pętli
# print()

# name = "Jarek"
# for letter in name:
    # print(letter)
# ta pętla powyżej bierze literę (zbieżność nazw zmiennej i jej roli) ze stringa przy każdym jej (tej pętli) powtórzeniu

# print()
# print(letter)
# a tu przykład, że po zakończeniu pętli zmienna w niej (w tej pętli) użyta zachowuje swoją wartość


# a tu najprostrzy zapis pętli for w C++ dla porównania:
# for (stanyPoczatkowe; warunekKoncowy; zmiany)
#   lista_instrukcji 

#  for (licznik=1;licznik<10;++licznik)
#    cout <<"Wykonuje petle po raz "<<licznik<<endl;
#
# źródło: http://drzewniak.slupsk.pl/~ks/c/c_013.html


expenses = []
aaa1 = (1, 2, 3)
aaa2 = (1, 2, 4)
aaa3 = (1, 2, 5)
aaa4 = (1, 2, 6)
aaa5 = (1, 2, 7)
expenses.append(aaa1)
expenses.append(aaa2)
expenses.append(aaa3)
expenses.append(aaa4)
expenses.append(aaa5)


def show_expenses(x):
    for a, b, c in expenses:
        print(a, b, c)
        if c == x:
            print(f'{a} - {b}')

show_expenses(3)