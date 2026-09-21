import sys
import string

polish_letters = ["ą", "Ą", "ć", "Ć", "ę", "Ę", "ł", "Ł", "ń", "Ń", "ó", "Ó", "ź", "Ź", "ż", "Ż"]
available_letters = string.ascii_lowercase + string.ascii_uppercase + "".join(polish_letters)
no_of_tries = 5
word = "kamila"
used_letters = []   # litery podane przez użytkownika
user_word = []      # lista w formie podkreślników, a w przypadku odgadnięcia litery zostają podmienione na nią 

for _ in word:
    user_word.append("_")

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print(" ".join(user_word))
    print("Pozostało żyć:", no_of_tries)
    print("Użyte litery:", ", ".join(used_letters) + ".")
    print()

###

print(" ".join(user_word))
print("Ilość żyć:", no_of_tries)
print()

while True:
    incorrectness_of_letter = True
    while incorrectness_of_letter:
        print("----------------------")
        letter = input("Podaj literę: ")
        letter = letter.lower()
        for i in available_letters:
            if i == letter:
                incorrectness_of_letter = False
                break
        else:
            print("To nie jest tylko jedna litera. Ponów próbę.")
        for j in used_letters:
            if j == letter:
                incorrectness_of_letter = True
                print("Ta litera została już wcześniej podana. Podaj inną.")
                break
        if incorrectness_of_letter == True:
            show_state_of_game()
    
    used_letters.append(letter)

    # print(word.index(letter))
    found_indexes = find_indexes(word, letter)    

    if len(found_indexes) == 0:
        print("W odgadywanym haśle nie ma takiej litery. Tracisz 1 życie!")
        no_of_tries -= 1
        
        if no_of_tries == 0:
            print("Koniec gry!")
            sys.exit(0)
    else:
        print("Brawo, ta litera znajduje się w odgadywanym haśle.")
        for index in found_indexes:  # przy każdym powtórzeniu pętli index przyjmuje wartość kolejnego elementu z listy
            user_word[index] = letter

    if "".join(user_word) == word:
        print("Brawo, to jest to słowo!")
        sys.exit(0)

    show_state_of_game()