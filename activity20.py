kdrama = []
isContinuing = True

while isContinuing:
    ans = input("Do you want to add a title of an kdrama (y/n): ") == "y"
    if ans == True:
        title = input("Enter the title of an anime: ")
        kdrama.append(title)
        print(kdrama)     
    else:
        isContinuing = False
        print(kdrama)