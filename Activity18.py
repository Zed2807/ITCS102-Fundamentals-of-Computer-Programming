#bool variable

tinutuloy = True

while tinutuloy == True:
    ask = input("Do you want to continue? (y/n): ")

    if ask.lower() == "yes":
        print("You chose to continue.")
        continue
    else:
        print("You chose to stop.")
        break