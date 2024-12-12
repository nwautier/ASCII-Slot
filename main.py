import datetime
import os
import random

# Define Global Variables
Hopper = int(500)
InCred = int(0)
OutCred = int(0)
Balance = int(0)
SpinCount = int(0)
JackPot = int(250)
ToPay = int(0)
ReelDisplay = str("0 0 0")
InfoStrip = "See your host to begin!"
UseConfig = "N"

# Set Reels (This does determine odds and payouts, so be smart!)
ReelA = ["J", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ReelB = ["J", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ReelC = ["J", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def AdminCheck():
    f = open("st.cfg", "r")
    p = str(f.readline().strip())
    x = str("")
    while x != p:
        os.system('cls' if os.name == 'nt' else 'clear')
        # User is stuck in the loop until Admin Password is entered.
        print("Enter the Administrative password to continue.")
        x = str(input(""))
        os.system('cls' if os.name == 'nt' else 'clear')
        if x == p:
            Log("Admin Pass Success")
            return True
        else:
            Log("Admin Pass Fail")
            print("Try Again")
    f.close()


def InputLoop(x):
    # This is the main loop that the program runs on.
    # Unless in the Service Menu, all key-presses are sent here for processing
    global InfoStrip, UseConfig
    if x == "":
        if Balance > 0:
            Spin()
        else:
            InfoStrip = "You need to put some credits in before you can spin...  See Your Host!"
    elif x == "DONE":
        # Launches an Admin Access page so proper hand-pay can be confirmed
        CredOut()
    elif x == "In":
        # Allows credits to be inserted to the system.  Perhaps needs security triggers?
        CredIn()
    elif x == "ServiceMenu":
        # Launches an Admin Access area with its own keypress capture loop
        ServiceMenu()
    elif x == "ShutDown":
        # Terminates the program immediately regardless of state.  Perhaps throw errors to pay-out or log current values first?
        Log("System ShutDown Requested")
        if UseConfig == "Y":
            WriteConfig()
        exit()
    else:
        # Catch-All term for any other input than those listed above.  Could be lost in future updates
        InfoStrip = "That feature is not yet supported!"


def CredIn():
    # Assumes that permission is granted and passed value can be cast to INT.
    global InCred, Hopper, Balance, SpinCount
    Log("InCred")
    if AdminCheck() is True:
        print("How many credits would you like to put in?")
        y = int(input())
        InCred += int(y)
        Hopper += int(y)
        Balance += int(y)
        Log("InCred")
    else:
        Log("Admin Pass Fail")


def CredOut():
    # Launches an Admin Access area to confirm hand pay
    x = 0
    global Hopper, Balance, OutCred
    Log("OutCred")
    os.system('cls' if os.name == 'nt' else 'clear')
    if AdminCheck() is True:
        print("Ending session with ", Balance, " credits!")
        x = input("Press Any Key")
        Hopper -= Balance
        OutCred += Balance
        Balance = 0
        Log("OutCred")
    else:
        Log("Admin Pass Fail")


def Spin():
    # Randomness and Payout is calculated here.  Simple System relies on Global Arrays to determine payout odds and odds of winning.
    global Balance, SpinCount, ReelDisplay, InfoStrip
    SpinCount += 1
    Balance -= 1

    x=1
    while x != 10:
        HitA = random.randrange(0,len(ReelA))
        HitB = random.randrange(0,len(ReelB))
        HitC = random.randrange(0,len(ReelC))
        ReelDisplay = (str(ReelA[HitA]) + " " + str(ReelB[HitB]) + " " + str(ReelC[HitC]))
        x += 1
        ScreenPrint()


    WinCalc(HitA, HitB, HitC)

def WinCalc(HitA, HitB, HitC):
    global Balance, SpinCount, ReelDisplay, InfoStrip
    ToPay = 0 # Local Variable
    if ReelA[HitA] == ReelB[HitB]: #First Two Match
        if ReelA[HitA] == ReelC[HitC]: #All Three Match
            if ReelA[HitA] == "J": #All Jackpot
                ToPay = JackPot
                Log("Jackpot "+ str(JackPot) + " Hit! S" + str(SpinCount))
            else: #All Three Match
                ToPay = 5 * ReelA[HitA]
        else: #First Two Match
            if ReelA[HitA] == "J": #First Two Jackpot
                ToPay=0
            else: #First Two Match, NOT Jackpot

                ToPay = 1 * ReelA[HitA]
        if ToPay > 0:
            InfoStrip = ("You Won " + str(ToPay) + " Credits")
            Balance += ToPay


def LoadConfig():
    global Hopper, InCred, OutCred, Balance, SpinCount, ReelA, ReelB, ReelC, JackPot
    f = open("bin.cfg", "r")
    Hopper = int(f.readline())
    InCred = int(f.readline())
    OutCred = int(f.readline())
    Balance = int(f.readline())
    SpinCount = int(f.readline())
    JackPot = int(f.readline())
    f.close()


def WriteConfig():
    global Hopper, InCred, OutCred, Balance, SpinCount, ReelA, ReelB, ReelC, JackPot
    f = open("bin.cfg", "w")
    f.write(str(Hopper) + "\n" + str(InCred) + "\n" + str(OutCred) + "\n" + str(Balance) + "\n" + str(SpinCount) + "\n" + str(JackPot))
    f.close()


def Log(x):
    f = open("verb.lg", "a")
    f.write(str(datetime.datetime.now()) + " " + x + "- H" + str(Hopper) + " I" + str(InCred) + " O" + str(OutCred) + " B" + str(Balance) + " S" + str(SpinCount) + " J" + str(JackPot) + "\n")
    f.close


def ScreenPrint():
    # Prints every time main loop is waiting for input.
    global ReelDisplay, Balance, InfoStrip
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ReelDisplay)
    print("Balance:", Balance)
    print(InfoStrip)
    InfoStrip = ""


def ServiceMenu():
    # NEEDS MUCH LOGGING
    # Lots more work to do here!!!
    Log("Service Menu Requested")
    global SpinCount, Hopper, InCred, OutCred, Balance
    x = 0
    if AdminCheck() is True:
        while x != "":
            # Not selecting any input, terminates Administrative mode.  A Typo brings you back to the same prompt
            print("Would you like to VIEW stats, SET hopper, or ADJUST balance?  Hit Return to exit.")
            x = input("")
            if x == "VIEW":
                print("SpinCount", SpinCount)
                print("Hopper:", Hopper)
                print("InCred:", InCred)
                print("OutCred:", OutCred)
                print("Balance:", Balance)
                print("JackPot:", JackPot)
                print("Profit:", int(int(InCred)-int(OutCred)-int(Balance)))
                print("Profit Per Spin:", int(int(InCred)-int(OutCred)-int(Balance))/int(SpinCount))
            elif x == "SET":

                print ("WARNING!  THIS WILL CHANGE THE HOPPER VALUE.  ARE YOU SURE YOU WOULD LIKE TO PROCEDE?")
                x=input("")

                if x == "YES":
                    print("How many credits are in the hopper?")
                    x = input()
                    Log("Admin Adjust Hopper " + str(Hopper) + " -> " + str(x) + " ")
                    Hopper = int(x)
            elif x == "ADJUST":
                print("Balance:", Balance, "How many to add?")
                x = input("")
                Log("Admin Adjust Balance " + str(Balance) + " -> " + str(x) + " ")
                Balance += int(x)


################# Application Starts Here #################
Log("Program Launch")
os.system('cls' if os.name == 'nt' else 'clear')
print("Load from config file?  N for Demo Mode")
UseConfig = input()
if UseConfig == "Y":
    LoadConfig()
    print(Hopper, InCred, OutCred, Balance, SpinCount, ReelA, ReelB, ReelC, JackPot)
    Log("Config Loaded")
else:
    Log("Demo Data Loaded")
    print("Demo Data Loaded")
print("Press any key to continue")
y = input()
print("")
while 1 > 0:
    # DUH...  FOREVER!
    ScreenPrint()
    x = input()
    InputLoop(x)  # " - S", SpinCount, "H", Hopper, "I", InCred, "O", OutCred, "B", Balance
