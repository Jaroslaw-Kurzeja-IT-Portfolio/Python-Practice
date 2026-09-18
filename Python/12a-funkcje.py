# 1:27:45

countries_information = {}
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)

# ta funkcja niczego nie zwraca / wykonuje (wyświetla) pewne operacje
def show_country_info(country):
    country_information = countries_information.get(country)
    print(type(country_information))
    print()
    print(country)
    print("-------------------")
    print("Stolica: " + country_information[0])
    print("Liczba mieszkańców (mln): " + str(country_information[1]))

for country in countries_information.keys():
    print(country)

country = input("Informację o jakim kraju chcesz wyświetlić? ")

if country.capitalize() in countries_information:
    show_country_info(country.capitalize())
else:
    print("takiego kraju nie ma w naszej bazie")


