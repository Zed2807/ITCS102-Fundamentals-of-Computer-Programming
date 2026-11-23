def my_factorial(answer):
    fact = 1
    for x in range (answer, 0, -1):
        fact *= x
    return fact

def greet_me(name):
    bati = "hi" + name
    return bati

def box(num):
    for x in range(num+1):
        for y in range(num+1):
            if x == 0 or y==0 or x== num or y == num:
                print(y, end = " ")
            else:
                print(" ",end=" ")
        print()
        
print("OUTPUT", my_factorial(1))
print("OUTPUT", my_factorial(2))
print("OUTPUT", my_factorial(3))
print("OUTPUT", my_factorial(4))
print("OUTPUT", my_factorial(5))

box(2)
box(5)
