from decimal import *
import os
import random

Hopper = int(500)
InCred = int(0)
OutCred = int(0)
Balance = int(0)
SpinCount = int(0)
ReelDisplay = str("0 0 0")
ErrorNotice = "See your host to begin!"
ToPay = int(0)

ReelA = [0,1,2,3]
ReelB = [0,1,2,3]
ReelC = [0,1,2,3]

def InputLoop(x):
    global ErrorNotice
    if x == "":
        if Balance > 0:
            Spin()
        else:
            ErrorNotice=("You need to put some credits in before you can spin...  See Your Host!")
    elif x == "DONE":
        CredOut()
    elif x == "In":
        print("How many credits would you like to put in?")
        x=int(input())
        CredIn(x)
    elif x=="ServiceMenu":
        ServiceMenu()
    elif x == "ShutDown":
        exit()
    else:
        ErrorNotice=("That feature is not yet supported!")

def CredIn(x):
    global InCred, Hopper, Balance
    InCred += int(x)
    Hopper += int(x)
    Balance += int(x)

def CredOut():
    x=0
    global Hopper, Balance, OutCred
    Hopper -= Balance
    OutCred += Balance
    os.system('cls' if os.name == 'nt' else 'clear')
    while x != "159753":
        print ("You have claimed", Balance, "Credits")
        print ("Enter the Administrative password to confirm claim.")
        x=input("")
        os.system('cls' if os.name == 'nt' else 'clear')
    Balance = 0

def Spin():
    global Balance, SpinCount, ReelDisplay, ErrorNotice
    SpinCount += 1
    Balance -= 1
    HitA = random.randrange(0,len(ReelA))
    HitB = random.randrange(0,len(ReelB))
    HitC = random.randrange(0,len(ReelC))

    ReelDisplay = (str(ReelA[HitA]) + " " + str(ReelB[HitB]) + " " + str(ReelC[HitC]))

    ToPay = 0
    if ReelA[HitA] == ReelB[HitB]:
        if ReelA[HitA] == ReelC[HitC]:
            ToPay = 5 * ReelA[HitA]
        else:
            ToPay = 1 * ReelA[HitA]
        if ToPay > 0:
            ErrorNotice = ("You Won " + str(ToPay) + " Credits")
    Balance += ToPay

def ScreenPrint():
    global ReelDisplay, Balance, ErrorNotice
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ReelDisplay)
    print("Balance:", Balance)
    print(ErrorNotice)
    ErrorNotice = ("")

def ServiceMenu():
    #NEEDS MUCH LOGGING
    global SpinCount, Hopper, InCred, OutCred, Balance
    x=0
    while x != "159753":
        print ("The Administrative password is required to continue.")
        x=input("")
        os.system('cls' if os.name == 'nt' else 'clear')
    while x != "":
        print ("Would you like to VIEW stats, SET hopper, or ADJUST balance?  Hit Return to exit.")
        x=input("")
        if x == "VIEW":
            print("SpinCount", SpinCount)
            print("Hopper:", Hopper)
            print("InCred:", InCred)
            print("OutCred:", OutCred)
            print("Balance:", Balance)
        elif x == "SET":
            print ("WARNING!  THIS WILL ERASE THE HOPPER VALUE.  ARE YOU SURE YOU WOULD LIKE TO PROCEDE?")
            x=input("")
            if x == "YES":
                print ("How many credits are in the hopper?")
                x=input()
                Hopper = int(x)
        elif x== "ADJUST":
            print("Balance:", Balance, "How many to add?")
            x=input("")
            Balance += int(x)
        else:
            ErrorNotice = ("Administrative Access Complete")
################# Application Starts Here #################

os.system('cls' if os.name == 'nt' else 'clear')
print("")
while 1>0:

    ScreenPrint()
    x = input()
    InputLoop(x)
