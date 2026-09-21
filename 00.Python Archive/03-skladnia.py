# składnia języka programowania (ang. syntax)
# czyli zbiór zasad określający w jaki sposób budować kod w danym języku

# Python to język DYNAMICZNIE i SILNIE typowany
# dynamicznie (np. Python) / statycznie typowany (np. Java)
# (typy zmiennych i argumentów sprawdzane są:
# - dynamicznie typowany - w momencie uruchamiania programu, gdy wykonywana jest konkretna linia kodu
# - statycznie typowany - w momencie kompilacji)
# wiąże się z tym, że gdy deklarujemy zmienną nie podajemy jej typu
# silne typowanie - typu zmiennej nie można już zmienić po jej zainicjalizowaniu

# Java - przykład składni w innym języku jak Python  

# int a = 5;
# int b = 2;

# if (a > b) {
#         System.Out.println("a jest większe od b");
# }

# funkcja "jeżeli"
a = input("podaj wartość a: ")
b = input("podaj wartość b: ")

if a > b:
    print("a jest większe od b")