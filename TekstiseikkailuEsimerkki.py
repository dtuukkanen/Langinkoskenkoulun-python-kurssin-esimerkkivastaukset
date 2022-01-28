# Tekstiseikkailut ovat pelejä, jotka nimensä mukaisesti toimivat tekstiin perustuvalla käyttöliittymällä. 
# Peli etenee sen mukaan, miten pelaaja vastaa esitettyihin kysymyksiin.
# Luo yksinkertainen tekstiseikkailupeli, joka koostuu erilaisista ehto- ja toistorakenteista.

print("You are in a dungeon. Your objective is to find a way out.")
print("")
print("The dungeon has one window, dungeon's door, toilet and bed.")
print("Where do you want search for a key?")

while(True):
    yritys = input("")
    if yritys == "bed":
        print("You found a key!")
        break
    elif yritys == "toilet":
        print("The toilet was empty, but dirty.")
        print("Try again!")
    elif yritys == "window":
        print("The window was barricated.")
        print("Try again!")
    else:
        print("Try again!")

print("Now you have a key. What do you want to do with it")

while(True):
    yritys = input("")
    if yritys == "open the door":
        break
    else:
        print("Try again!")

print("Door opened!")
print("Now you have to escape. What do you want to do?")

while(True):
    yritys = input("")
    if yritys == "run run run":
        break
    elif yritys == "walk" or yritys == "run":
        print("Guard caught you!")
        print("Try again!")
    else:
        print("Try again!")

print("Congratulations!")
print("You succesfully escaped the dungeon!")