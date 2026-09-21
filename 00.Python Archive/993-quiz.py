import json

points = 0

def show_question(question):
    global points
    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Którą odpowiedź wybierasz? ")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("To prawidłowa odpowiedź, brawo! Ilość Twoich punktów:", points)

    else:
        print("Niestety to zła odpowieź.")
        print("Prawidłowa odpowiedź to:", question["prawidlowa_odpowiedz"], "(" + str(question[question["prawidlowa_odpowiedz"]]) + ").")

with open("quiz.json") as json_file:
    questions = json.load(json_file)

print(questions)

for i in range(0, len(questions)):
    show_question(questions[i])

print("To koniec gry. Zdobyta liczba punktów to: "+ str(points) + ".")










