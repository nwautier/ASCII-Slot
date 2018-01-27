from decimal import *
import os

Hopper = int(500)
InCred = int(0)
OutCred = int(0)
Balance = int(0)

def InputLoop(x):
    if x == "":
        if Balance > 1:
            Spin()
        else:
            print("You need to put some credits in before you can spin...  See Your Host!")
    elif x == "DONE":
        CredOut()
    elif x == "In":
        print("How many credits would you like to put in?")
        x=int(input())
        CredIn(x)
    else:
        print("That feature is not yet supported!")

def CredIn(x):
    global InCred, Hopper, Balance
    InCred = InCred + int(x)
    Hopper = Hopper + int(x)
    Balance = Balance + int(x)

def CredOut():
    x=0
    global Hopper, Balance, OutCred
    Hopper =  Hopper -  Balance
    OutCred = OutCred + Balance
    Balance = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    while x != "159753":
        print ("You have claimed", Balance, "Credits")
        x=input("Enter the password to confirm claim.")

################# Application Starts Here #################

while 1>0:
    os.system('cls' if os.name == 'nt' else 'clear')

    ##### DEBUG LINES #####
    print("Hopper:", Hopper)
    print("InCred:", InCred)
    print("OutCred:", OutCred)
    print("Balance:", Balance)
    ##### DEBUG LINES #####

    print("Press Enter to Spin")
    print("Type DONE to End Your Session")
    x = input()
    InputLoop(x)
