direction=input("Would you like to go 'left' or 'right'?\n").lower()
if direction=="right":
    lake=input("You have arrived at a lake.\nType 'swim' or 'wait'\nWait will wait for boat\n").lower()
    if lake=="wait":
        doors=input("YOu have arrived at an island!\n"
                    "There is a house with three doors\n"
                    "Choose which one to open\n"
                    "'red', 'yellow' or 'blue'\n").lower()
        if doors=="yellow":
            print("You found the treasure!!")
        elif doors=="red":
            print("You have walked in a room of fire!!\nGame over!!")
        elif doors=="blue":
            print("You have walked in a room of ice!\n"
                  "You are freezing to death!!"
                  "Game Over!!")
        else:
            print(f"{doors.title()} is not an option. \nGame Over!!")
    elif lake=="swim":
        print("You have been eaten by piranhas!!\nGame Over!!")
    else:
        print(f"{lake.title()} is not an appropriate option.\nGame Over!!")
elif direction=="left":
    print("You fell in a hole!\nGame Over!!")
else:
    print(f"{direction.title()} is not an option.\nGame Over!!")