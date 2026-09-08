#import demo
import getpass

username = "Zedrick"
password = "Umbrete"

u = input("Input Enter your username: ")
p = getpass.getpass("Input Enter your password: ")  
if u == username and p == password:
    print("Access granted")
else:
    print("Access denied")