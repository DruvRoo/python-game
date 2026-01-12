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
        self.gold = 250
        self.hpPotion = 3
        self.room = 0
p = player()

# ====== Enemy Stat Setup ====== #
class Enemy:
    def __init__(self, name, hp, dmg, critC, critM, dodge):
        self.name = name
        self.hp = hp
        self.hpMax = hp
        self.dmg = dmg
        self.critC = critC
        self.critM = critM
        self.dodge = dodge
        
####                   ####
#### ==== ENEMIES ==== ####
####                   ####
# SET 1
def goblin():
    return Enemy("Goblin", 25, 5, 0.05, 1.25, 0.05)
def kobold():
    return Enemy("Kobold", 20, 7, 0.15, 1.25, 0.05 )
def bandit():
    return Enemy("Bandit", 30, 6, 0.20, 1.5, 0.10)
def boar():
    return Enemy("Boar", 50, 5, 0.05, 1.25, 0.05)
# SET 2

## ENEMY SCALING ##
def spawn_enemy(template_func, room):
    e = template_func()   # new Enemy

    scale = 1 + room * 0.50

    e.hp = round(int(e.hp * scale), 2)
    e.hpMax = e.hp
    e.dmg = round(int(e.dmg * scale), 2)

    return e


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
        player.critM = 1.15
        player.dodge = 0.05
        player.dmg = 10
        player.gold = 250
    elif player.role == "assassin":
        player.hp = 60
        player.hpMax = 60
        player.dodge = 0.2
        player.critC = 0.25
        player.critM = 1.5
        player.dmg = 6
        player.gold = 250
    elif player.role == "archer":
        player.hp = 50
        player.hpMax = 50
        player.dodge = 0.3
        player.critC = 0.2
        player.critM = 1.25
        player.dmg = 8
        player.gold = 250

    os.system('cls')
    intro1 = f"You are now called {player.name} the {player.role.capitalize()}!\n"
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    rooms()

###                                      ###
### ========== Game Over part ========== ###
###                                      ###
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
def hpPot(enemy):
    global Enemy
    if p.hpPotion <= 0:
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
        print("You're out of Health Potions!")
    else:
        tempHP = player.hp
        player.hp = player.hp + (player.hpMax * 0.25)
        if player.hp > player.hpMax:
            player.hp = player.hpMax
        healedHP = player.hp - tempHP
        p.hpPotion -= 1

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
        if p.hpPotion == 0:
            print(f"You've healed {healedHP} HP!")
            print(f"You have no more Health Potions left!")
        else:
            print(f"You've healed {healedHP} HP!")
            print(f"You have {p.hpPotion} Health Potions left!")
    time.sleep(2)
    enemyATK(enemy)

####                   ###
#### === BATTLE UI === ###
####                   ###
def battleUI(enemy):
    global Enemy
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
    battleUItemp(enemy)
def battleUItemp(enemy):
    global Enemy
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
               playerATK(enemy)
            if choice == 2:
                if player.hp == player.hpMax:
                    print("You already have max HP!")
                    battleUItemp(enemy)
                else:
                    hpPot(enemy)
            if choice == 3:
                playerINSP(enemy)
            if choice == 4:
                playerDEF(enemy)
            else:
                input("Invalid input. Press Enter to try again.")
                battleUItemp(enemy)
        except ValueError:
            input("Invalid input. Press Enter to try again.")
            battleUItemp(enemy)

# ================================================== #
#####                            #####
##### ===== BATTLE ACTIONS ===== #####
#####                            #####

###                           ###
### === Enemy Attack Turn === ###
###                           ###
def enemyATK(enemy):
    global Enemy
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
            finalDMGenemy = random.randint(enemy.dmg - 3, enemy.dmg + 3)

            if isCrit:
                finalDMGenemy *= enemy.critM
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
            
            ### final dmg
            player.hp -= round(finalDMGenemy, 2)
            if player.hp <= 0:
                player.hp = 0
                print(f"The {enemy.name} has dealt {finalDMGenemy}!")
                time.sleep(0.5)
                gameOver()
            os.system('cls')
            player.hp = round(player.hp, 2)
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
            print(f"The {enemy.name} has dealt {finalDMGenemy}!")
        time.sleep(0.5)
        input("\nPress Enter to continue.")
    battleUItemp(enemy)

###                            ###
### === Player Attack Turn === ###
###                            ###
def playerATK(enemy):
    # Player attack
    global Enemy
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
        finalDMGplayer = random.randint(player.dmg - 1, player.dmg + 4)

        if isCrit:
            finalDMGplayer *= player.critM
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
        enemy.hp -= round(finalDMGplayer, 2)
        if enemy.hp <= 0:
            enemy.hp = 0
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
            print(f"You have dealt {finalDMGplayer}!\n")
            time.sleep(1)
            print("You Win!")
            time.sleep(0.5)
            input("\n\nPress Enter to continue.")
            rewards()
        
        os.system('cls')
        enemy.hp = round(enemy.hp, 2)
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
    enemyATK(enemy)

###                          ###
### ===== Defense Turn ===== ###
###                          ###
def playerDEF(enemy):
    global Enemy
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
    print("You raised your guard.")
    time.sleep(1)
    # enemy dmg calc -> defense reduce final dmg -> enemy final dmg output

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
            finalDMGenemy = random.randint(enemy.dmg - 3, enemy.dmg + 3)

            if isCrit:
                finalDMGenemy *= enemy.critM
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
            
            ## Final DMG cut in half due to guard
            finalDMGenemy /= 2
            player.hp -= round(finalDMGenemy, 2)
            if player.hp <= 0:
                player.hp = 0
                print(f"The {enemy.name} has dealt {finalDMGenemy}!")
                time.sleep(1)
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
            print(f"The {enemy.name} has dealt {finalDMGenemy}!")
        time.sleep(0.5)
        input("\nPress Enter to continue.")
    battleUItemp(enemy)

###                           ###
### ===== Enemy Inspect ===== ###
###                           ###
def playerINSP(enemy):
    global Enemy
    # should tell the name, hp, dmg, crit chance and multi, and the dodge chance of the enemy
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

    inspectStats = (
            f"Enemy: {enemy.name}\n"
            f"Damage range: {enemy.dmg - 3} ~ {enemy.dmg + 3}\n"
            f"Crit Chance: {enemy.critC * 100}%\n"
            f"Crit Multiplier: {enemy.critM}x\n"
            f"Dodge Chance: {enemy.dodge * 100}%\n\n"
                )
    for char in inspectStats:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

    time.sleep(1)
    input("Press Enter to continue.")
    battleUItemp(enemy)

# ================================================== #

###                        ###
### === REWARDS SYSTEM === ###
###                        ###
def rewards():
    os.system('cls')
    gold = random.randint(20, 40)
    p.gold += gold
    print(f"You gained {gold} gold!")
    time.sleep(1)

    print("You leveled up!")
    time.sleep(1)
    print("You gained:")
    time.sleep(1)
    print("[Increased DMG!]")
    time.sleep(0.5)
    print("[Increased MAX HP!]")
    time.sleep(0.5)
    print("[Healed to MAX HP!]")
    time.sleep(0.5)
    if p.role == "warrior":
        p.dmg += 5
        p.hpMax += 15
    if p.role == "assassin":
        p.dmg += 2 
        p.hpMax += 8
        p.critM += 0.05
        print("[Minor CRIT MULTIPLIER increase!]")
    if p.role == "archer":
        p.dmg += 3
        p.hpMax += 10
        p.critC += 0.02
        print("[Minor CRIT CHANCE increase!]")
    
    p.dmg *= 1.15
    p.hpMax *= 1.15
    round(p.dmg, 2)
    round(p.hpMax, 2)
    p.hp = p.hpMax    

    p.room += 1
    input("\nPress Enter to continue.")
    rooms()

###                          ###
### ==== Special Events ==== ###
###                          ###
def merchant():
    os.system('cls')
    intro = f"You run into a travelling merchant!"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    os.system('cls')
    intro = f"Do you want to buy items from the merchant?\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    choiceMer = input("Yes or No?: ")
    validChoice = ["yes", "no"]
    while choiceMer not in validChoice:
        print("Invalid role, please try again.")
        time.sleep(1)
        os.system('cls')
        print("Do you want to buy items from the merchant?\n")
        choiceMer = input("Yes or No?: ")
    match choiceMer:
        case "yes":
            merchantShop()
        case "no":
            intro = f"You decided not to buy from the travelling merchant and continued on your path. . .\n"
            for character in intro:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            p.room += 1
            rooms()
def merchantShop():
    os.system('cls')
    shopUI1 = (
        "===================================================================\n"
        "                 What do you want to buy, traveller?               \n"
        "===================================================================\n"
            )
    for char in shopUI1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
    shopUI2 = (
        "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
        "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
        "===================================================================\n"
        f"Gold Amount: {p.gold} Gold\n\n"
            )
    for char in shopUI2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(1)
    shopUI3 = (
        "Type the number of the item of your choice, or stop buying.\n"
            )
    for char in shopUI3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
    merchantShopTemp()

    ##
def merchantShopTemp():
    product1 = 100
    product2 = 250
    product3 = 200

    os.system('cls')
    shopUI4 = (
        "===================================================================\n"
        "                 What do you want to buy, traveller?               \n"
        "===================================================================\n"
        "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
        "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
        "===================================================================\n"
        f"Gold Amount: {p.gold} Gold\n\n\n"
        "Type the number of the item of your choice, or stop buying."
            )
    print(shopUI4)
    merchantChoice = int(input("‣ "))
    validChoice = [1, 2, 3, 4]

    while merchantChoice not in validChoice:
        print("Invalid choice, try again.")
        time.sleep(2)
        os.system('cls')
        shopUI4 = (
        "===================================================================\n"
        "                 What do you want to buy, traveller?               \n"
        "===================================================================\n"
        "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
        "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
        "===================================================================\n"
        f"Gold Amount: {p.gold} Gold\n\n\n"
        "Type the number of the item of your choice, or stop buying."
            )
        print(shopUI4)
        merchantChoice = int(input("‣ "))

    ### Items for shop ###
    match merchantChoice:
        case 1:
            ## Health Pot
            if p.gold < product1:
                print("Insufficient gold.")
                time.sleep(1)
                merchantShopTemp()
            os.system('cls')
            shopUI4 = (
                "===================================================================\n"
                "                 What do you want to buy, traveller?               \n"
                "===================================================================\n"
                "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                "===================================================================\n"
                f"Gold Amount: {p.gold} Gold\n\n"
                    )
            print(shopUI4)
            choiceBuy = input("Buying Health Potion: Confirm? (y or n): ")
            validChoice = ["y", "Y", "n", "N"]

            while choiceBuy not in validChoice:
                print("Invalid choice, try again.")
                time.sleep(1)
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                    "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n"
                    )
                print(shopUI4)
                choiceBuy = input("Buying Health Potion: Confirm? (Y or N): ")
            
            ## Yes or No
            if choiceBuy == "y" or choiceBuy == "Y":
                p.gold -= product1
                p.hpPotion += 1
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                    "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n"
                    )
                print(shopUI4)
                print(f"You now have {p.hpPotion} Health Potion/s!")
                input("Press Enter to continue.")
                merchantShopTemp()
            if choiceBuy == "n" or choiceBuy == "N":
                merchantShopTemp()
        case 2:
            ## Power Up Necklace
            if p.gold < product2:
                print("Insufficient gold.")
                time.sleep(1)
                merchantShopTemp()
            os.system('cls')
            shopUI4 = (
                "===================================================================\n"
                "                 What do you want to buy, traveller?               \n"
                "===================================================================\n"
                "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                "===================================================================\n"
                f"Gold Amount: {p.gold} Gold\n\n"
                    )
            print(shopUI4)
            choiceBuy = input("Buying Power Up Necklace: Confirm? (y or n): ")
            validChoice = ["y", "Y", "n", "N"]

            while choiceBuy not in validChoice:
                print("Invalid choice, try again.")
                time.sleep(1)
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                    "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n"
                    )
                print(shopUI4)
                choiceBuy = input("Buying Power Up Necklace: Confirm? (Y or N): ")
            
            ## Yes or No
            if choiceBuy == "y" or choiceBuy == "Y":
                p.gold -= product2
                p.dmg += 2
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                    "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n"
                    )
                print(shopUI4)
                print(f"Your DMG increased by 2!")
                input("Press Enter to continue.")
                merchantShopTemp()
            if choiceBuy == "n" or choiceBuy == "N":
                merchantShopTemp()
        case 3:
            ## HP Necklace
            if p.gold < product3:
                print("Insufficient gold.")
                time.sleep(1)
                merchantShopTemp()
            os.system('cls')
            shopUI4 = (
                "===================================================================\n"
                "                 What do you want to buy, traveller?               \n"
                "===================================================================\n"
                "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                "===================================================================\n"
                f"Gold Amount: {p.gold} Gold\n\n"
                    )
            print(shopUI4)
            choiceBuy = input("Buying HP Necklace: Confirm? (y or n): ")
            validChoice = ["y", "Y", "n", "N"]

            while choiceBuy not in validChoice:
                print("Invalid choice, try again.")
                time.sleep(1)
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                    "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n"
                    )
                print(shopUI4)
                choiceBuy = input("Buying HP Necklace: Confirm? (Y or N): ")
            
            ## Yes or No
            if choiceBuy == "y" or choiceBuy == "Y":
                p.gold -= product3
                p.hp += 10
                p.hpMax += 10
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                    "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n"
                    )
                print(shopUI4)
                print(f"Your HP increased by 10!")
                input("Press Enter to continue.")
                merchantShopTemp()
            if choiceBuy == "n" or choiceBuy == "N":
                merchantShopTemp()
        case 4:
            ## Quit
            p.room += 1
            os.system('cls')
            shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion (100 Gold)        3 • HP Necklace (200 Gold)\n"
                    "2 • Power Up Necklace (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n"
                    )
            print(shopUI4)
            print("You decided to continue on your journey. . .")
            time.sleep(1)
            p.hp = p.hpMax
            rooms()
def end():
    pass

####                         ####
#### ===== ROOM SETUPS ===== ####
####                         ####

## ROOM PICKER ##
def rooms():
    match p.room:
        case 0:
            room1()
        case 1:
            room2()
        case 2:
            merchant()
        case 3:
            room3()
        case 4:
            room4()
        case 5:
            merchant()
        case 6:
            boss()
        case 7:
            end()

## ROOM LISTS ##
def room1():
    global Enemy
    os.system('cls')
    intro = f"You venture out into the wilderness. . .\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    enemySet1 = random.randint(1, 4)
    match enemySet1:
        case 1:
            enemy = spawn_enemy(goblin, p.room)
        case 2:
            enemy = spawn_enemy(kobold, p.room)
        case 3:
            enemy = spawn_enemy(bandit, p.room)
        case 4:
            enemy = spawn_enemy(boar, p.room)
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

    battleUI(enemy) 

def room2():
    global Enemy
    os.system('cls')
    print("The enemies got stronger!")
    os.system('cls')
    intro = f"You venture out into the wilderness. . .\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    enemySet1 = random.randint(1, 4)
    match enemySet1:
        case 1:
            enemy = spawn_enemy(goblin, p.room)
        case 2:
            enemy = spawn_enemy(kobold, p.room)
        case 3:
            enemy = spawn_enemy(bandit, p.room)
        case 4:
            enemy = spawn_enemy(boar, p.room)
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

    battleUI(enemy)  

def room3():
    global Enemy
    os.system('cls')
    print("The enemies got stronger!")
    os.system('cls')
    intro = f"You venture out into the wilderness. . .\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    enemySet1 = random.randint(1, 4)
    match enemySet1:
        case 1:
            enemy = spawn_enemy(goblin, p.room)
        case 2:
            enemy = spawn_enemy(kobold, p.room)
        case 3:
            enemy = spawn_enemy(bandit, p.room)
        case 4:
            enemy = spawn_enemy(boar, p.room)
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

    battleUI(enemy)  

def room4():
    global Enemy
    os.system('cls')
    print("The enemies got stronger!")
    os.system('cls')
    intro = f"You venture out into the wilderness. . .\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    enemySet1 = random.randint(1, 4)
    match enemySet1:
        case 1:
            enemy = spawn_enemy(goblin, p.room)
        case 2:
            enemy = spawn_enemy(kobold, p.room)
        case 3:
            enemy = spawn_enemy(bandit, p.room)
        case 4:
            enemy = spawn_enemy(boar, p.room)
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

    battleUI(enemy)  

def boss():
    print("Damn, it's the boss")
    input("Enter to continue.")

titleScreen()