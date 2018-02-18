from decimal import *
import os
import random

# Define Global Variables
Hopper = int(500)
InCred = int(0)
OutCred = int(0)
Balance = int(0)
SpinCount = int(0)
ToPay = int(0)
ReelDisplay = str("0 0 0")
InfoStrip = "See your host to begin!"

# Set Reels (This does determine odds and payouts, so be smart!)
ReelA = [0,1,2,3]
ReelB = [0,1,2,3]
ReelC = [0,1,2,3]


def InputLoop(x):
    # This is the main loop that the program runs on.  Unless in the Service Menu, all keypresses are sent here for processing
    global InfoStrip
    if x == "":
        if Balance > 0:
            Spin()
        else:
            InfoStrip=("You need to put some credits in before you can spin...  See Your Host!")
    elif x == "DONE":
        # Launches an Admin Access page so they can confirm proper hand-pay
        CredOut()
    elif x == "In":
        # Allows credits to be inserted to the system.  Perhaps needs security triggers?
        print("How many credits would you like to put in?")
        x=int(input())
        CredIn(x)
    elif x=="ServiceMenu":
        # Launches an Admin Access area with its own keypress capture loop
        ServiceMenu()
    elif x == "ShutDown":
        # Terminates the program imediately regardless of state.  Perhaps throw errors to pay-out or log current values first?
        exit()
    else:
        # Catch-All term for any other input than those listed above.  Could be lost in future updates
        InfoStrip=("That feature is not yet supported!")

def CredIn(x):
    # Assumes that permission is granted and passed value can be cast to INT.
    global InCred, Hopper, Balance
    InCred += int(x)
    Hopper += int(x)
    Balance += int(x)

def CredOut():
    # Launches an Admin Access area to confirm hand pay
    x=0
    global Hopper, Balance, OutCred
    os.system('cls' if os.name == 'nt' else 'clear')
    while x != "159753":
        # User is stuck in the loop until Admin Password is entered.
        print ("You have claimed", Balance, "Credits")
        print ("Enter the Administrative password to confirm claim.")
        x=input("")
        os.system('cls' if os.name == 'nt' else 'clear')
    Hopper -= Balance
    OutCred += Balance
    Balance = 0

def Spin():
    # Randomness and Payout is calculated here.  Simple System relies on Global Arrays to determine payout odds and odds of winning.
    global Balance, SpinCount, ReelDisplay, InfoStrip
    SpinCount += 1
    Balance -= 1
    HitA = random.randrange(0,len(ReelA))
    HitB = random.randrange(0,len(ReelB))
    HitC = random.randrange(0,len(ReelC))

    ReelDisplay = (str(ReelA[HitA]) + " " + str(ReelB[HitB]) + " " + str(ReelC[HitC]))

    ToPay = 0 # Local Variable
    if ReelA[HitA] == ReelB[HitB]:
        if ReelA[HitA] == ReelC[HitC]:
            ToPay = 5 * ReelA[HitA]
        else:
            ToPay = 1 * ReelA[HitA]
        if ToPay > 0:
            InfoStrip = ("You Won " + str(ToPay) + " Credits")
    Balance += ToPay

def ScreenPrint():
    # Prints every time main loop is waiting for input.
    global ReelDisplay, Balance, InfoStrip
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ReelDisplay)
    print("Balance:", Balance)
    print(InfoStrip)
    InfoStrip = ("")

def ServiceMenu():
    # NEEDS MUCH LOGGING
    # Lots more work to do here!!!
    global SpinCount, Hopper, InCred, OutCred, Balance
    x=0
    while x != "159753":
        print ("The Administrative password is required to continue.")
        x=input("")
        os.system('cls' if os.name == 'nt' else 'clear')
    while x != "":
        # Not selecting any input, terminates Administrative mode.  A Typo brings you back to the same prompt
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
            Balance += int()

################# Application Starts Here #################

os.system('cls' if os.name == 'nt' else 'clear')
print("")
while 1>0:
    # DUH...  FOREVER!
    ScreenPrint()
    x = input()
    InputLoop(x)
