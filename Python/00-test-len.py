a = "jeden" # string
b = "2"       # integer
c = "3.3"     # float
d = [1, 22, 3, "cztery"]      # list
e = (1, 22, 3)      # tuple
f = set()   # set
g = {}      # dictionary
h1 = "zzz"

aaa = [a, b, c, d, e, f, g, h1]

for x in aaa:
    print(x)
    print(len(x))
    print("--------")

# wniosek:
# dla wszystkich powyższych typ zmiennych można użyć metodę len() - poza int i float (TypeError)