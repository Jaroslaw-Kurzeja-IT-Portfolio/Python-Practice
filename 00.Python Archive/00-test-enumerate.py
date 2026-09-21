# x = [1, 2, 3]
# print(enumerate(x)) # display: <enumerate object at 0x0000020D9B23F8C0>

# zzz = ["a", "b", "c", "d"]
# print(type(enumerate(zzz))) # display: <class 'enumerate'>

# zzz = ["a", "b", "c", "d"]
# print(list(enumerate(zzz))) # display: [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# zzz = ["a", "b", "c", "d"]
# aaa = list(enumerate(zzz))
# print(type(aaa[0])) # display: <class 'tuple'>

# zzz = []
# x = input("Podaj literę 'x': ")
# for a, b in enumerate("kamila"):
#     if x == b:
#         print("to jest 'a':", a)
#         print("to jest 'b':", b)
#         zzz.append(a)
# print("to jest lista 'zzz':", zzz)

# for index, letter_in_word in enumerate(word):
#         if letter == letter_in_word:
#             indexes.append(index)

# bbb = (1, 2, 3, 4)
# aaa = list(bbb)
# print(aaa)
# Podsumowując: co robi funkcja 'list()'
# - przyjmuje tylko jeden argument
# - zamienia argument na listę, np tuple-->list, enumarete-->list

# aaa = (1, 2, 3, 4)
# aaa = list(aaa)
# print(aaa)
# aaa = tuple(aaa)
# print(aaa)
# aaa = set(aaa)
# print(aaa)
# aaa = list(aaa)
# print(aaa)
# aaa = dict(aaa) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# print(aaa)

# aaa = [1, 2, 3, 4]
# print(aaa) # display: [1, 2, 3, 4]
# print(list(enumerate(aaa))) # display: [(0, 1), (1, 2), (2, 3), (3, 4)]

# aaa = (1, 2, 3, 4)
# print(aaa) # display: (1, 2, 3, 4)
# print(list(enumerate(aaa))) # display: [(0, 1), (1, 2), (2, 3), (3, 4)]
# # Wniosek 1: obojętnie czy lista czy krotka, funkcja enumerate pobiera elementy z obiektu i numeruje je
# # Wniosek 2: funkcja enumerate zwraca dziwną wartość/obiekt, dlatego trzeba ten obiekt "ubrać" w listę/krotkę/itd

# aaa = (1, 2, 3, 4)
# print(aaa) # display: (1, 2, 3, 4)
# print(list(enumerate(aaa, start = 3))) # display: [(0, 1), (1, 2), (2, 3), (3, 4)]
# # Wniosek 3: po argumencie można podać "start = x", aby funkcja ta zaczęła numerować od wartości 'x'

# ddd = {"1": "jeden", "2": "dwa"}
# print(list(enumerate(ddd)))  # display: [(0, '1'), (1, '2')]

# aaa =  ["a", "b", "c", "d"]
# print(aaa) # display: ['a', 'b', 'c', 'd']
# print(dict(enumerate(aaa, start = 5))) # display: {5: 'a', 6: 'b', 7: 'c', 8: 'd'}