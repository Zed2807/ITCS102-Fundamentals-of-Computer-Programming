def my_factorial(sagot):
    fact = 1
    for x in range(sagot, 0, -1):
        fact *= x
    return fact

def greet_me(name):
    bati = "hi " + name
    return bati

def box(num):
    for x in range(num + 1):
        for y in range(num + 1):
            if x == 0 or y == 0 or x == num or y == num:
                print(y, end=" ")
            else:
                print(" ", end=" ")
        print()

# Sample function calls
print("output", my_factorial(13))
print("output", my_factorial(7))
print("output", my_factorial(8))
print("output", my_factorial(5))
print("output", my_factorial(21))

print(greet_me("Leonard"))
print(greet_me("Michelle"))

# Menu loop
while True:
    choose = int(input("Enter choice (1-4): "))

    if choose == 1:
        print("FACTORIAL")
        num = int(input("Enter a any number "))
        print(my_factorial(num))
    elif choose == 2:
        print("GREETINGS")
        name = input("Enter a any name ")
        print(greet_me(name))
        continue
    elif choose == 3:
        print("BOX")
        num = int(input("Enter a box size "))
        box(num)
        continue
    elif choose == 4:
        print("SYSTEM EXIT")
        break
    else:
        print("invalid choice ")

box(2)
box(5)