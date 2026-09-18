import string

# print(dir(string))

# for i in dir(string):
#     print(i)
#     print(getattr(string, i))
#     print()

# for i in dir(string):
#     print(i)

# display:
# print(string.Formatter()) # display: <class 'string.Formatter'> / Formatter() takes no arguments / <string.Formatter object at 0x000001C474CE82B0>
# print(string.Template("Aaa")) # display: <string.Template object at 0x000001C840CE82E0> / 'Template' object is not iterable
# print(type(string._ChainMap())) # display: <class 'collections.ChainMap'> / ChainMap({})
# print(string.__all__) # to jest: lista / ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace', 'Formatter', 'Template']
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# _re
# _sentinel_dict
# _string
# print(string.ascii_letters) # string:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# ascii_lowercase # to jest: string z małymi literami
# ascii_uppercase # to jest: string z dużymi literami
# print(string.capwords("aAa bbB")) # to jest: funkcja zmieniająca wszystkie słowa! w stringu w myśl: Aaa Bbb itd. 
# btw: print(type("aAa bbB".capitalize())) # to jest: metoda zmieniająca pierwszą literę w stringu na duża, a reszta małe
# print(string.digits)      # string: 0123456789
# print(string.hexdigits)   # string: 0123456789abcdefABCDEF
# print(string.octdigits)   # string: 01234567
# print(string.printable)   # string: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~♂♀
# print(string.punctuation) # string: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(list(enumerate(string.whitespace))) # [(0, ' '), (1, '\t'), (2, '\n'), (3, '\r'), (4, '\x0b'), (5, '\x0c')]
# print("\t") --> działa jak podwójny tab używając spacji
# print("\n") --> nowa linia
# print("\r") --> carriage return pl: powrót katetki / cofa kursor na początek aktualnej linii i pisze po już zapisanych znakach
# print("abcj0" + "\r" + "kiszt")
