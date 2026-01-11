### === THE CODE IS NOT OPTIMIZED === ###
# I can't optimize the code since I started studying python at the start of January, so I'm still new with it.
# I did watch a tutorial on how to make a game which is linked below:
# https://www.youtube.com/watch?v=MFW8DJ6qsak&list=PL1-slM0ZOosXf2oQYZpTRAoeuo0TPiGpm&index=1


import cmd
import textwrap
import sys
import os
import time
import random

# ====== Player Setup ====== #
class player:
    ## == Your Character == ##
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.hpMax = 0
        self.dmg = 0
        self.role = ""
        self.dodge = 0
        self.critC = 0
        self.critM = 1.5
        self.wepType = ""
        self.wepQuality = ""
        self.gold = 0


# ====== Enemy Stat Setup ====== #
class enemy:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.hpMax = 0
        self.dmg = 0
        self.statusEffects = []
        self.wep = "Fists"
        self.dodge = 0
        self.critC = 0
        self.critM = 1.5
        

#### ==== ENEMIES ==== ####
def goblin():
    enemy.name = "Goblin"
    enemy.hp = random.randint(20, 30)
    enemy.hpMax = enemy.hp
    enemy.dmg = random.randint(5, 10)
    enemy.dodge = 0.15
    enemy.critC = 0.05



### ============ WEAPONS ============ ###
weapons = {
    "Old": {
        "Sword": {"dmg": 4},
        "Staff": {"dmg": 2},
        "Dagger": {"dmg": 3},
        "Bow": {"dmg": 3}
    },
    "Average": {
        "Sword": {"dmg": 9},
        "Staff": {"dmg": 6},
        "Dagger": {"dmg": 8},
        "Bow": {"dmg": 7}
    },
    "Quality": {
        "Sword": {"dmg": 15},
        "Staff": {"dmg": 12},
        "Dagger": {"dmg": 14},
        "Bow": {"dmg": 13}
    }
}

###                            ###
### ====== Title Screen ====== ###
###                            ###
def titleScreenSelection():
    optionTitle = input("• ")
    if optionTitle.lower() == ("play"): 
        setupGame() 
    elif optionTitle.lower() == ("help"):
        helpMenu()
    elif optionTitle.lower() == ("tips"):
        tipsMenu()
    elif optionTitle.lower() == (""):
        titleScreen()
    elif optionTitle.lower() == ("quit"):
        sys.exit()
    while optionTitle.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command.")
        time.sleep(2)
        titleScreen()

def titleScreen():
    os.system('cls')
    print("===================================")
    print(" Welcome to your » Average Game! « ")
    print("===================================")
    print("             - Play -              ")
    print("             - Help -              ")
    print("             - Tips -              ")
    print("             - Quit -              ")
    print("===================================")
    titleScreenSelection()

def helpMenu():
    os.system('cls')
    print("=========================================")
    print("     Welcome to your » Average Game! « ")
    print("=========================================")
    print("   ‣ Type the commands to do them.        ")
    print("   ‣ Press Enter if you're done.     ")
    print("=========================================")
    titleScreenSelection()

def tipsMenu():
    os.system('cls')
    print("=========================================")
    print("     Welcome to your » Average Game! «   ")
    print("=========================================")
    print("‣ The Warrior class is a good role for beginners!")
    print("‣ Press Enter if you're done.          ")
    print("=========================================")
    titleScreenSelection()

def gameOver():
    os.system('cls')
    gameOverText = "G A M E   O V E R . . ."
    for char in gameOverText:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.75)
    input("\n\nPress Enter to go back to the menu.")
    titleScreen()

###                                      ###
### ============ Health Pot ============ ###
###                                      ###
def hpPot():
    tempHP = player.hp
    player.hp = player.hpMax * 1.25
    if player.hp > player.hpMax:
        player.hp = player.hpMax
    healedHP = player.hp - tempHP
    os.system('cls')
    fightUI1 = (
                "========================================\n"
                f"{player.name}: {player.hp}/{player.hpMax}\n"
                f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
                "========================================\n"
                )
    fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Heal               4 • Defend\n"
                )
    print(fightUI1)
    print(fightUI2)
    print(f"You've healed {healedHP} HP!")
    time.sleep(2)
    enemyATK()

####                   ###
#### === BATTLE UI === ###
####                   ###
def battleUI():
    os.system('cls')
    fightUI1 = (
        "========================================\n"
        f"{player.name}: {player.hp}/{player.hpMax}\n"
        f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
        "========================================\n"
            )

    for char in fightUI1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

    fightUI2 = (
            "1 • Attack             3 • Inspect\n"
            "2 • Heal               4 • Defend\n"
            )

    for char in fightUI2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
    battleUItemp()

###                           ###
### === Enemy Attack Turn === ###
###                           ###
def enemyATK():
    if enemy.hp > 0:
        if random.random() < player.dodge:
            os.system('cls')
            fightUI1 = (
                "========================================\n"
                f"{player.name}: {player.hp}/{player.hpMax}\n"
                f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
                "========================================\n"
                )
            fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Heal               4 • Defend\n"
                )
            print(fightUI1)
            print(fightUI2)
            print(f"The {enemy.name} missed!")
        else:
            isCrit = random.random() < enemy.critC
            finalDMGenemy = enemy.dmg

            if isCrit:
                finalDMGenemy = enemy.dmg * enemy.critM
                os.system('cls')
                fightUI1 = (
                    "========================================\n"
                    f"{player.name}: {player.hp}/{player.hpMax}\n"
                    f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
                    "========================================\n"
                    )
                fightUI2 = (
                    "1 • Attack             3 • Inspect\n"
                    "2 • Heal               4 • Defend\n"
                    )
                print(fightUI1)
                print(fightUI2)
                print(f"\nThe {enemy.name} hit a CRITICAL HIT!!")
                time.sleep(1)
            
            ### finaldmg
            player.hp -= finalDMGenemy
            if player.hp <= 0:
                player.hp = 0
                print(f"The {enemy.name} has dealt {enemy.dmg}!")
                time.sleep(0.5)
                gameOver()
            os.system('cls')
            fightUI1 = (
                "========================================\n"
                f"{player.name}: {player.hp}/{player.hpMax}\n"
                f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
                "========================================\n"
                    )
            fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Heal               4 • Defend\n"
                    )
            print(fightUI1)
            print(fightUI2)    
            print(f"The {enemy.name} has dealt {enemy.dmg}!")
        time.sleep(0.5)
        input("\nPress Enter to continue.")
    battleUItemp()

## == Player Attack Choice == ##
def playerATK():
    # Player attack
    if random.random() < enemy.dodge:
        os.system('cls')
        fightUI1 = (
                "========================================\n"
                f"{player.name}: {player.hp}/{player.hpMax}\n"
                f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
                "========================================\n"
                )
        fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Heal               4 • Defend\n"
                )
        print(fightUI1)
        print(fightUI2)
        print("You missed!")
    else:
        isCrit = random.random() < player.critC
        finalDMGplayer = player.dmg

        if isCrit:
            finalDMGplayer = player.dmg * player.critM
            os.system('cls')
            fightUI1 = (
                "========================================\n"
                f"{player.name}: {player.hp}/{player.hpMax}\n"
                f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
                "========================================\n"
                    )
            fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Heal               4 • Defend\n"
                    )
            crit = "You've dealt a CRITICAL HIT!!"
            print(fightUI1)
            print(fightUI2)
            print(crit)
            time.sleep(1)

        ### finaldmg
        enemy.hp -= finalDMGplayer
        if enemy.hp <= 0:
            enemy.hp = 0
            print(f"You have dealt {finalDMGplayer}!")
            time.sleep(1)
            os.system('cls')
            fightUI1 = (
                "========================================\n"
                f"{player.name}: {player.hp}/{player.hpMax}\n"
                f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
                "========================================\n"
                    )
            fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Heal               4 • Defend\n"
                    )
            print(fightUI1)
            print(fightUI2)

            print("You Win!")
            time.sleep(0.5)
            input("\n\nPress Enter to continue.")
            rewards()
        
        os.system('cls')
        fightUI1 = (
            "========================================\n"
            f"{player.name}: {player.hp}/{player.hpMax}\n"
            f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
            "========================================\n"
            )
        fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Heal               4 • Defend\n"
                )
        print(fightUI1)
        print(fightUI2)
        print(f"You have dealt {finalDMGplayer}!")

    time.sleep(2)
    enemyATK()

def battleUItemp():
    while enemy.hp > 0 and player.hp > 0:
        os.system('cls')
        fightUI1 = (
            "========================================\n"
            f"{player.name}: {player.hp}/{player.hpMax}\n"
            f"{enemy.name}: {enemy.hp}/{enemy.hpMax}\n"
            "========================================\n"
            )
        fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Heal               4 • Defend\n"
                )
        print(fightUI1)
        print(fightUI2)
        
        try:
            choice = int(input("What do you want to do?: "))
            if choice == 1:
               playerATK()
            if choice == 2:
                hpPot()
            if choice == 3:
                pass
            if choice == 4:
                pass
            else:
                input("Invalid input. Press Enter to try again.")
                battleUItemp()
        except ValueError:
            input("Invalid input. Press Enter to try again.")
            battleUItemp()



###                          ###
### ==== Special Events ==== ###
###                          ###
def specialEvent1():
    specialEncounter1 = random.randit(1,20)
    if specialEncounter1 == 1:
        boss()
    else:
        goblin()

####                         ####
#### ===== ROOM SETUPS ===== ####
####                         ####
def room1():
    enemySet1 = random.randint(1, 5)
    match enemySet1:
        case 1:
            goblin()
        case 2:
            goblin()
        case 3:
            goblin()
        case 4:
            goblin()
        case 5:
            goblin()
    os.system('cls')
    intro1 = f"You have encountered a {enemy.name}!"
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)  

    time.sleep(1)
    os.system('cls')
    time.sleep(0.4)
    print(intro1)
    time.sleep(0.4)
    os.system('cls')
    time.sleep(0.4)
    print(intro1)
    time.sleep(0.4)
    os.system('cls')
    time.sleep(0.4)
    print(intro1)
    time.sleep(0.4)

    battleUI() 


def room2():
    enemySet1 = random.randint(1, 4)
    if enemySet1 == 1:
        goblin()
    if enemySet1 == 2:
        kobold()
    if enemySet1 == 3:
        bandit()
    if enemySet1 == 4:
        boar()

def room3():
    pass

def room4():
    pass

def room5():
    pass

def room6():
    pass

def room7():
    pass

def room8():
    pass

def room9():
    pass

def bossRoom():
    pass

##                      ##
## ==== Game Setup ==== ##
##                      ##
def setupGame():
    os.system('cls')

    # == Name == #
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input("‣ ")
    player.name = playerName

    # == Class == #
    os.system('cls')
    question2 = f"Good day, {player.name}! What role do you want to play?\n"
    question2add = "You can play as a Warrior, Assassin, or Archer.\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.035)
    for character in question2add:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)
    playerRole = input("‣ ")
    validRoles = ["warrior", "assassin", "archer"]

    while playerRole not in validRoles:
        print("Invalid role, please try again.")
        time.sleep(1)
        os.system('cls')
        print(f"Good day, {player.name}! What role do you want to play?")
        print("You can play as a Warrior, Assassin, or Archer.")
        playerRole = input("‣ ")
    
    player.role = playerRole
    if player.role == "warrior":
        player.hp = 80
        player.hpMax = 80
        player.critC = 0.05
        player.dodge = 0.05
        player.dmg = random.randint(7, 10)
        player.gold = 250
    elif player.role == "assassin":
        player.hp = 60
        player.hpMax = 60
        player.dodge = 0.2
        player.critC = 0.25
        player.critM = 2.25
        player.dmg = random.randint(1, 12)
        player.gold = 250
    elif player.role == "archer":
        player.hp = 50
        player.hpMax = 50
        player.dodge = 0.3
        player.critC = 0.2
        player.critM = 2.0
        player.dmg = random.randint(2, 8)
        player.gold = 250

    os.system('cls')
    intro1 = f"You are now called {player.name} the {player.role.capitalize()}!\n"
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)

    os.system('cls')
    intro = f"You venture out into the wilderness. . .\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    room1()
    


titleScreen()