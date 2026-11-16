#Part1

pssnger = ["Neill", "kien", "Nico"]

pssnger.append("Zed")
pssnger.insert(0, "Lolo")
pssnger.remove("kien")
x = pssnger.pop()
y = pssnger.pop(0)
len(pssnger)
"Neill" in pssnger
pssnger.reverse()
print(pssnger)

#Part2 interactive

rota = ["Terminal", "DLL", "PACIFIC MALL"]
pssnger = []
seat = 6
fare = 12
total = 0

while True:
    print()
    print("sakay:", pssnger)
    print(len(pssnger), "of", seat, "seats")
    print("1 Sakay\n2 Priority seat\n3 PARA PO!")
    print("4 baba sa pinto\n5 baba sa harap")
    print("6 seat check\n7 balikan\n88 exit")
    choice = input("choice: ")

    if choice == "1":
        if len(pssnger) == seat:
            print("PUNO NA!")
        else:
            name = input("NAME: ")
            pssnger.append(name)
            total = total + fare
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(pssnger) == seat:
            print("PUNO NA!")
        else:
            name = input("NAME: ")
            pssnger.insert(0, name)
            total = total + fare
            print(name, "Took the priority seat.")

    elif choice == "3":
        name = input("Who is getting off? ")
        if name in pssnger:
            pssnger.remove(name)
            print(name, "Got off. INGAT!")
        else:
            print(name, "Is not on this jeep.")

    elif choice == '4':
        if len(pssnger) == 0:
            print('The jeep is empty')
        else:
            left = pssnger.pop()
            print(left, "Got of at the door.")

    elif choice == "5":
        if len(pssnger) == 0:
            print("THE JEEP IS EMPTY")
        else:
            front = pssnger.pop(0)
            print(front, "Got off at the front")

    elif choice == "6":
        for i in range(len(pssnger)):
            print("seat", i + 1, pssnger[1])

    elif choice == "7":
        rota.reverse()
        print("route: ", rota)

    elif choice == "8":
        print("Total fare today: ", total)
        break

    else:
        print("INVALID CHOICE!")
