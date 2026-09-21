import string
import sys

# Walidacja dla Quiz (a, b, c, d):

# a = input("podaj cyfrę: ")

# if a != "a" or "b" or "c" or "d":
#     print("Nierozpoznana odpowiedź. Podaj a, b, c lub d.")


# Walidacja dla Wisielca (wszystkie litery alfabetu):
# polskie_litery = ["ą", "Ą", "ć", "Ć", "ę", "Ę", "ł", "Ł", "ń", "Ń", "ó", "Ó", "ź", "Ź", "ż", "Ż"]
# x = True
# while x:
#     podana_litera = input("Podaj literę: ")
#     for i in string.ascii_lowercase and string.ascii_uppercase and polskie_litery:
#         if i == podana_litera:
#             x = False
#             break
#     else:
#         print("To nie jest litera. Podaj jedną literę.")

polish_letters = ["ą", "Ą", "ć", "Ć", "ę", "Ę", "ł", "Ł", "ń", "Ń", "ó", "Ó", "ź", "Ź", "ż", "Ż"]
available_letters = string.ascii_lowercase + string.ascii_uppercase + "".join(polish_letters)
print(available_letters)

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

# for i in dir(string):
#     a = "string." + i
#     print(a)

# Walidacja dla Generatora Haseł przy podawaniu ilości (liczba; i to może tylko z wybranego zakresu):



