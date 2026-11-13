#TARGET 1

loan = float(input("Input how much you loan --->  "))
yrs = int(input("Input how many years ---> "))

mths = yrs * 12
prncipal = loan / mths
rem_bal = loan
print(f"Months\t|   Monthly Payment\t|\tInterest\t|\tPrincipal\t|\tRemaining Loan")

for x in range(1, mths + 1):
    intr = rem_bal * 0.0025
    pay = prncipal + intr
    rem_bal = rem_bal - prncipal
    if rem_bal < 0.005:
        bal = 0.0
    print(f"{x}\t|\t{round(pay, 2,)}\t\t|\t{round(intr, 2)}\t\t|\t{round(prncipal, 2)}\t\t|\t{round(rem_bal, 2)}")
print()
#TARGET 2
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

row = int(input("input the size of your triangle ---> "))
for x in range(row - 1):
  for y in range(2 * row - 1):
    if y == row - 1 - x or y == row - 1 + x:
      print("*", end= " ")
    else:
      print(" ", end= " ")
  print()
print("* " * (2 * row - 1))
print()
#TARGET 3
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

ruw = int(input("Input the of your size Z:"))
for x in range(ruw):
  for y in range(ruw):
    if x == 0 or x == ruw -1 or y == ruw -1 -x:
      print("*", end= " ")
    else:
      print(" ", end= " ")
  print()