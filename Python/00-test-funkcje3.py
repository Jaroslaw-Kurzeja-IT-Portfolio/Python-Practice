a = 10
b = 10
print("to jest wartość zmiennej 'a' PRZED użyciem funkcji aaa(a, b): " + str(a))
print("to jest wartość zmiennej 'b' PRZED użyciem funkcji aaa(a, b): " + str(b))
print("----------------------")
def aaa():
    print("to jest wartość zmiennej 'a' WEWNĄTRZ funkcji aaa(a, b): " + str(a+1))
    print("to jest wartość zmiennej 'b' WEWNĄTRZ funkcji aaa(a, b): " + str(b+1))
    print("----------------------")
    
    return a, b

c = aaa()
a = c[0]
b = c[1]

print("----------------------")
print("to jest wartość zmiennej 'a' PO użyciu funkcji aaa(a, b): " + str(a))
print("to jest wartość zmiennej 'b' PO użyciu funkcji aaa(a, b): " + str(b))

