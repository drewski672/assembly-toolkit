import math
import msvcrt as m

#Main Menu

def mainmenu():
    print("\n\n\n\n\nWelcome to the Equilibar assembly toolkit!\n\n\nPlease make a selection from the menu!")
    choice = input("1: Torque Converter\n2: Leak Test and Overpressure Calculator\n")
    if choice == ("1"):
        torqueMenu()
    elif choice == ("2"):
        pressureCalc()

#Torque Converter Menu

def torqueMenu():
    choice = input("\n\nWhich conversion would you like?\n1: In lbs to Ft lbs\n2: Ft lbs to In lbs\n")
    if choice == ("1"):
        inToFt()
    elif choice == ("2"):
        ftToIn()

#Converts inch pounds to foot pounds

def inToFt():
    value = input("\n\nEnter a value in inch pounds:")
    print(value + " inch pounds is " + str(float(value)/12) + " foot pounds.\n\n")
    wait()

#Converts foot pounds to inch pounds

def ftToIn():
    value = input("\n\nEnter a value in foot pounds:")
    print(value + " foot pounds is " + str(float(value)*12) + " inch pounds.\n\n")
    wait()

#Leak test and overpressure calculator

def pressureCalc():
    number = input("\n\nWhat is the rated pressure?:  ")
    diaphragmCheck = input("Metal diaphragm? (y/n)\n")
    if diaphragmCheck == ("y"):
        print("Leak test at: ")
        print(str(float(number)) + " psi.\n")
        print("2% overpressure is: ")
        print(str(float(number) - float(number) * .02) + " psi.\n")
        print("5% overpressure is: ")
        print(str(float(number) - float(number) * .05) + " psi.\n")
    elif diaphragmCheck == ("n"):
        print("Leak test at: ")
        print(str(float(number) * 1.5) + " psi.\n")
        print("2% overpressure is: ")
        print(str(float(number) - float(number) * .02) + " psi.\n")
        print("5% overpressure is: ")
        print(str(float(number) - float(number) * .05) + " psi.\n")
    wait()

#Cues user to press enter to continue

def wait():
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    mainmenu()

    

mainmenu()
    
    
