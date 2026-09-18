# 1:35:50
# aby nie pojawił się błąd, który kończyłby działanie programu. chcemy ten błąd obsłużyć.
# przechwycić odpowiedni wyjątek. obsłużyć ten wyjątek.

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}

try:
    print(2 / 0)
    print(countries_and_capitals['USA'])
except KeyError:
    print("nie ma takiego państwa")
except ZeroDivisionError:
    print("ZeroDivisionError")

# blok finally wykorzystywany jest zazwyczaj do tego, aby zamknąć zasoby (gdy wcześniej zostały otwarte połączenia do plików, bazy danych)
finally:
    print("blok finally wyświetli się zawsze")

print("111111")

try:
    print(countries_and_capitals['USA'])
except:
    print("nie ma takiego państwa")

print("2222222")
