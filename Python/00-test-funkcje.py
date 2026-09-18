a = 10
b = 10
aaa_list = []
print("to jest wartość zmiennej 'a' PRZED użyciem funkcji aaa(a, b): " + str(a))
print("to jest wartość zmiennej 'b' PRZED użyciem funkcji aaa(a, b): " + str(b))
print("----------------------")
def aaa():
    a = 1
    b = 2
    print("to jest wartość zmiennej 'a' WEWNĄTRZ funkcji aaa(a, b): " + str(a))
    print("to jest wartość zmiennej 'b' WEWNĄTRZ funkcji aaa(a, b): " + str(b))
    print("----------------------")
    aaa_list = [a, b]

    return aaa_list
aaa_list = aaa()
a = aaa_list[0]
b = aaa_list[1]

print("----------------------")
print("to jest wartość zmiennej 'a' PO użyciu funkcji aaa(a, b): " + str(a))
print("to jest wartość zmiennej 'b' PO użyciu funkcji aaa(a, b): " + str(b))
print("to zwraca funkcja aaa_list: " + str(aaa_list))
