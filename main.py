from decimal import *
import os
import random
import datetime

Hopper = int(500)
InCred = int(0)
OutCred = int(0)
Balance = int(0)
SpinCount = int(0)

ReelA = [0,1,2,3]
ReelB = [0,1,2,3]
ReelC = [0,1,2,3]

def InputLoop(x):
    if x == "":
        if Balance > 0:
            Spin()
        else:
            print("You need to put some credits in before you can spin...  See Your Host!")
    elif x == "DONE":
        CredOut()
    elif x == "In":
        print("How many credits would you like to put in?")
        x=int(input())
        CredIn(x)
    elif x == "ShutDown":
        exit()
    else:
        print("That feature is not yet supported!")

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
        print ("Enter the password to confirm claim.")
        x=input("")
        os.system('cls' if os.name == 'nt' else 'clear')
    Balance = 0

def Spin():
    global Balance, SpinCount
    SpinCount += 1
    Balance -= 1
    HitA = random.randrange(0,len(ReelA))
    HitB = random.randrange(0,len(ReelB))
    HitC = random.randrange(0,len(ReelC))
    os.system('cls' if os.name == 'nt' else 'clear')

    # print(ReelA[HitA-1],ReelB[HitB-1],ReelC[HitC-1]) #
    print(ReelA[HitA],ReelB[HitB],ReelC[HitC])
    # print(ReelA[HitA+1],ReelB[HitB+1],ReelC[HitC+1]) #

    if ReelA[HitA] == ReelB[HitB]:
        if ReelA[HitA] == ReelC[HitC]:
            Balance += 5 * ReelA[HitA]
        else:
            Balance += 1 * ReelA[HitA]
def Log(x):
    f = open("log.txt", "a")
    f.write(str(datetime.datetime.now()) + " " + x + "\n")
    f.close
################# Application Starts Here #################
Log("Program Launch")
os.system('cls' if os.name == 'nt' else 'clear')
print("")
while 1>0:

    ##### DEBUG LINES #####
    print("SpinCount", SpinCount)
    print("Hopper:", Hopper)
    print("InCred:", InCred)
    print("OutCred:", OutCred)
    print("Balance:", Balance)
    ##### DEBUG LINES #####

    print("Press Enter to Spin")
    print("Type DONE to End Your Session")
    x = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    InputLoop(x)
