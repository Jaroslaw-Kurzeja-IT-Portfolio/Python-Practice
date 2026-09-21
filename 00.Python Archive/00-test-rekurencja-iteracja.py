# Iteracja (łac. iteratio – powtarzanie):
# Czynność powtarzania tej samej operacji w pętli z góry określoną liczbę razy lub aż do spełnienia określonego warunku.
# Mianem iteracji określa się także operacje wykonywane wewnątrz takiej pętli. 

# Rekurencja, rekursja (z łac. recurrere, przybiec z powrotem):
# Odwoływanie się funkcji lub definicji do samej siebie. 

# -------------------------------------------------------
# Funkcje iteracyjne i rekurencyjne obliczające silnię:

# # iteracja 1 - przy pomocy pętli while:
# def silnia_i(n):
#     i = 0
#     s = 1
#     while i < n:
#         i += 1
#         s = s * i
#     return s

# # iteracja 2 - przy pomocy pętli for:
# def silnia_i2(n):
#     s = 1
#     for i in range(1, n+1):
#         s = s * i
#     return s

# # rekurencja
# def silnia_r(n):
#     if n == 0:
#         w = 1
#     else:
#         w = n * silnia_r(n - 1)
#     return w


# n = 5
# print(silnia_i(n))
# print(silnia_i2(n))
# print(silnia_r(n))

# ----------------------------------

# # funkcje rekurencyjne wyświetlające liczby: (od a do z co 1) oraz (od z do a co 1)
# # nie można wykorzystać pętli while i for

# def odliczanie_od_x(z):
#     if z == a:
#         print(z)
#     else:
#         print(z)
#         odliczanie_od_x(z - 1)
#     return

# def dodawanie_od_a_do_x(a):
#     global z
#     if a == z:
#         print(a)
#     else:
#         print(a)
#         a = dodawanie_od_a_do_x(a + 1)
#     return a

# a = 4
# z = 10
# dodawanie_od_a_do_x(a)
# odliczanie_od_x(z)

#  def silnia_r(n):
#     if n == 0:
#         w = 1
#     else:
#         w = n * silnia_r(n - 1)
#     return w

# def nazwa_funkcji(start):
#     global koniec
#     if start == koniec:
#         print(start)
#     else:
#         print(start)
#         start = nazwa_funkcji(start - 1)
#     return start

# start = 10
# koniec = 5
# nazwa_funkcji(start)