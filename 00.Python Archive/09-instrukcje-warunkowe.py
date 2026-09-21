light = input("jakie jest światło? (green, red, yellow) ")


if light == 'red':
# nie musi być operator porównania. Ważne, aby została zwrócona wartość bool.
    print("czekaj!")
elif light == "yellow":
    print("szykuj się!")
elif light == "green":
    print("jedź!")    
else:
    print("niewłaściwa wartość")


print ("jedź!") if light == "green" else print("czekaj!")