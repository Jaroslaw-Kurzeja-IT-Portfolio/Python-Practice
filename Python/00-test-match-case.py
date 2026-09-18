# def aaa(x):
#     match x:
#         case 1:
#             return "jeden"
#         case 2:
#             return "dwa"
#         case 3:
#             return "trzy"
#         case 4:
#             return "cztery"
#         case 5:
#             return "pięć"
        
# x = int(input("Podaj liczbę (1-5): "))
# print(aaa(x))

# input zapisuje wszystko jako str (nawet cyfry)
# y = print(type(input("wciśnij 5: ")))
# print(y)
# funkcja print() nic nie zwraca

# ------------------------------------------
# Zadanie:

# point = (0, 75)

# match point:
#     case (x, y) if x == 0 and y > 50:
#         print("ok")
#     case _:
#         print("nie ok")

a = 10

if a > 11:
    print("a > 11")
elif a > 2:
    print("a > 2")
elif a > 3:
    print("a > 3")
elif a == 10 :
    print("a = 10")
# Wniosek: elif jest podobny do match case pod tym względem, że jeżeli spełniony jest jakiś warunek, to reszta zostaje pominięta

