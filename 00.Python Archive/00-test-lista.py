moja_lista = []
moja_lista.append("jeden")
moja_lista.append("dwa")
moja_lista.append("trzy")
moja_lista.append("cztery")
moja_lista.append("pięć")

moja_lista[2] = "skowronek"
print(moja_lista.remove("cztery"))


print(moja_lista)

for razdwatrzy in moja_lista:
    print(razdwatrzy)

print(type(moja_lista))

# łączenie list:
moja_lista2 = ["aaa", "bbb", "ccc"]
# moja_lista3 = moja_lista.union(moja_lista2)     - AttribureError: 'list' object has no attribute 'union'
# czyli pozostaje połączenie przy pomocy pętli for (po jednym elemencie), tzn.:

moja_lista3 = moja_lista
for element in moja_lista2:
    print(element)
    moja_lista3.append(element)
print(moja_lista3)