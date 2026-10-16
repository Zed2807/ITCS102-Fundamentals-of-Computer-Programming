
#machine 1
for x in range(1,5):
    for y in range(1,x): 
        print(y,end = "")
    print("",x)
#machine 2
for z in range(1,5):
    for d in range(1, z + 1): 
        print(d,end = " ")
    print("--", z)