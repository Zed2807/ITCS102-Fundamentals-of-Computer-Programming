def my_factorial(answer):
    fact = 1
    for x in range (answer, 0, -1):
        fact *= x
    return fact

def greet_me(name):
    bati = "hi" + name
    return bati

print("OUTPUT", my_factorial(1))
print("OUTPUT", my_factorial(2))
print("OUTPUT", my_factorial(3))
print("OUTPUT", my_factorial(4))
print("OUTPUT", my_factorial(5))
