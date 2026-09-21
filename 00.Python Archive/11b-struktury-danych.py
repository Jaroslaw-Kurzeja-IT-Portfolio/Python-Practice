# tuple - krotka
# można wyświetlić długość krotki, jak często występuje element w krotce, wyświetlić dany element


names_list = ("Kamil", "Mariusz", "Adam", "Kamil")

print("tak wygląda ta krotka: " + str(names_list))

print("\nIlość elementów: " + str(len(names_list)))

print("\nPozycja elementu 'Kamil': " + str(names_list.count("Kamil")))
print("Pozycja elementu 'Kamil': " + str(names_list.count("Adam")))

print("\nElement z pozycją nr 2: " + names_list[1] + "\n")

for name in names_list: # przy każdym powtórzeniu pętli 'name' przyjmuje wartość kolejnego elementu krotki
    print(name + " " + str(type(name)))
