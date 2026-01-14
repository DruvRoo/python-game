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
        self.gold = 250
        self.hpPotion = 3
        self.room = 0
        self.hpPotUp = False
        self.guard = False
p = player()

# ====== Enemy Stat Setup ====== #
class Enemy:
    def __init__(self, name, hp, dmg, critC, critM, dodge, charge=0):
        self.name = name
        self.hp = hp
        self.hpMax = hp
        self.dmg = dmg
        self.critC = critC
        self.critM = critM
        self.dodge = dodge
        self.charge = charge
        
####                   ####
#### ==== ENEMIES ==== ####
####                   ####
# SET 1
def goblin():
    return Enemy("Goblin", 25, 5, 0.05, 1.25, 0.05)
def kobold():
    return Enemy("Kobold", 20, 7, 0.15, 1.25, 0.05)
def bandit():
    return Enemy("Bandit", 30, 6, 0.20, 1.5, 0.10)
def boar():
    return Enemy("Boar", 50, 5, 0.05, 1.25, 0.05)
# SET 2
def knight():
    return Enemy("Knight", 60, 9, 0.05, 1.25, 0.05)
def archer():
    return Enemy("Archer", 45, 7, 0.2, 1.25, 0.15)
def assassin():
    return Enemy("Assassin", 30, 7, 0.15, 1.5, 0.2)
def wolf():
    return Enemy("Wolf", 50, 8, 0.05, 1.25, 0.05)
# BOSS
def dragon():
    return Enemy("Dragon", 75, 5, 0.05, 1.25, 0, 0)

## ENEMY SCALING ##
def spawn_enemy(template_func, room):
    e = template_func()   # new Enemy

    scale = 1 + room * 0.25

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
    validRoles = ["warrior", "assassin", "archer", "testing"]

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
    ## TESTING PURPOSES ##
    elif player.role == "testing":
        player.hp = 500
        player.hpMax = 500
        player.dodge = 0.5
        player.critC = 0.5
        player.critM = 1.5
        player.dmg = 1
        player.gold = 900

    os.system('cls')
    intro1 = f"You are now called {player.name} the {player.role.capitalize()}!\n"
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    rooms()
def victoryScreen():
    os.system('cls')
    
    victory_text = [
        "====================================",
        "        YOU HAVE WON THE GAME        ",
        "====================================",
        "",
        "The Dragon has been defeated!",
        "The kingdom is finally safe.",
        "",
        "You are a true hero.",
        "",
        "Press Enter to return to the title..."
    ]

    for line in victory_text:
        print(line)
        time.sleep(0.3)

    input()
    titleScreen()
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
        if p.hpPotUp == True:
            player.hp = player.hp + (player.hpMax * 0.50)
        else:
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
    player.hp = round(player.hp, 2)
    player.hpMax = round(player.hpMax, 2)
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
            elif choice == 2:
                if player.hp == player.hpMax:
                    print("You already have max HP!")
                    bossBattleUItemp(enemy)
                else:
                    hpPot(enemy)
            elif choice == 3:
                playerINSP(enemy)
            elif choice == 4:
                playerDEF(enemy)
            else:
                input("Invalid input. Press Enter to try again.")
                bossBattleUItemp(enemy)
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
        finalDMGplayer = random.randint(int(player.dmg) - 1, int(player.dmg) + 4)

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
            if enemy.name == "Dragon":
                victoryScreen()
        
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
    if enemy.charge == 1:
        bossATK(enemy)
    elif enemy.name == "Dragon":
        bossATK(enemy)
    else:
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
    if enemy.charge == 1:
        p.guard = True
        bossATK(enemy)
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
    if enemy.name == "Dragon":
        bossBattleUItemp(enemy)
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
    
    ## If dragon is charging
    if enemy.charge == 1:
        print("The dragon is charging something, it's best to guard against it.\n")
        time.sleep(1)
        input("Press Enter to continue.")
        bossBattleUItemp(enemy)

    time.sleep(1)
    input("Press Enter to continue.")
    battleUItemp(enemy)

# ================================================== #

###                        ###
### === REWARDS SYSTEM === ###
###                        ###
def rewards():
    global player
    os.system('cls')
    if p.room == 0:
        gold = random.randint(20, 40)
    if p.room == 1:
        gold = random.randint(35, 50)
    if p.room == 3:
        gold = random.randint(75, 100)
    if p.room == 4:
        gold = random.randint(100, 125)
    
    p.gold += gold
    print(f"You gained {gold} gold!")
    time.sleep(1)
    os.system('cls')

    print("You leveled up!\n")
    time.sleep(1)
    print("You gained:")
    time.sleep(1)
    print("[Increased DMG!]")
    time.sleep(0.5)
    print("[Increased MAX HP!]")
    time.sleep(0.5)
    if player.role == "warrior":
        player.dmg += 4
        player.dmg += (p.room * 0.25)
        player.hpMax += 20
    if player.role == "assassin":
        player.dmg += 5
        player.dmg += (p.room * 0.25)
        player.hpMax += 8
        player.critM += 0.05
        print("[Minor CRIT MULTIPLIER increase!]")
    if player.role == "archer":
        player.dmg += 6
        player.dmg += (p.room * 0.25)
        player.hpMax += 12
        player.critC += 0.02
        print("[Minor CRIT CHANCE increase!]")
    
    player.dmg *= 1.1
    player.hpMax *= 1.35
    round(p.dmg, 2)
    round(p.hpMax, 2)
    round(player.dmg, 2)
    round(player.hpMax, 2)

    p.room += 1
    input("\nPress Enter to continue.")
    rooms()

###                          ###
### ==== BOSS BATTLE UI ==== ###
###                          ###
def bossBattleUI(enemy):
    global Enemy
    player.hp = round(player.hp, 2)
    player.hpMax = round(player.hpMax, 2)
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
    bossBattleUItemp(enemy)
def bossBattleUItemp(enemy):
    global Enemy
    global player
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
            elif choice == 2:
                if player.hp == player.hpMax:
                    print("You already have max HP!")
                    bossBattleUItemp(enemy)
                else:
                    hpPot(enemy)
            elif choice == 3:
                playerINSP(enemy)
            elif choice == 4:
                playerDEF(enemy)
            else:
                input("Invalid input. Press Enter to try again.")
                bossBattleUItemp(enemy)
        except ValueError:
            input("Invalid input. Press Enter to try again.")
            bossBattleUItemp(enemy)
def bossATK(enemy):
    global Enemy
    global player
    if enemy.hp > 0:
        chances = random.randint(1, 2)
        if chances != 1:
            pass
        else:
            if enemy.charge == 1:
                pass
            else:
                specialATK(enemy)


        ## Charged atk
        if enemy.charge == 1:
            finalDMGenemy = (random.randint(enemy.dmg - 5, enemy.dmg + 5)) * 2
            if p.guard == True:
                finalDMGenemy *= 0.15
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
                print(f"You raised your guard.")
                time.sleep(1)
            player.hp -= round(finalDMGenemy, 2)
            if player.hp <= 0:
                player.hp = 0
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
                print(f"The {enemy.name} used Fire Breath!")
                time.sleep(1)
                print(f"The {enemy.name} has dealt {finalDMGenemy}!")
                time.sleep(1)
                p.guard = False
                enemy.charge -= 1

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
            print(f"The {enemy.name} used Fire Breath!")
            time.sleep(1)
            print(f"The {enemy.name} has dealt {finalDMGenemy}!")
            time.sleep(1)
            input("Press Enter to continue.")
            enemy.charge -= 1
            if p.guard == True:
                p.guard = False
            bossBattleUItemp(enemy)
            
            
            



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
            finalDMGenemy = round(finalDMGenemy, 2)
            player.hp -= finalDMGenemy
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
    bossBattleUItemp(enemy)
def specialATK(enemy):
    # Order: Player atks -> boss charges atk -> Player option -> boss atks -> goes back to temp UI
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
    print(f"The {enemy.name} is charging up a Fire Breath!\n")
    time.sleep(1)
    enemy.charge += 1
    input("Press Enter to continue.")
    bossBattleUItemp(enemy)

###                          ###
### ==== Special Events ==== ###
###                          ###
# First Merchant
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
        print("Invalid choice, please try again.")
        time.sleep(1)
        os.system('cls')
        print("Do you want to buy items from the merchant?\n")
        choiceMer = input("Yes or No?: ")
    match choiceMer:
        case "yes":
            merchantShop()
        case "no":
            os.system('cls')
            intro = f"You decided not to buy from the travelling merchant and continued on your path. . .\n"
            for character in intro:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            p.room += 1
            time.sleep(1)
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
            rooms()

# Second Merchant
def merchant2():
    os.system('cls')
    intro = f"You come across a small shop while going around the castle."
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    os.system('cls')
    intro = f"The person running the store calls you in, he doesn't look like an enemy."
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    os.system('cls')
    intro = f"Do you want to buy items from the man?\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    choiceMer = input("Yes or No?: ")
    validChoice = ["yes", "no"]
    while choiceMer not in validChoice:
        print("Invalid choice, please try again.")
        time.sleep(1)
        os.system('cls')
        print("Do you want to buy items from the man?\n")
        choiceMer = input("Yes or No?: ")
    match choiceMer:
        case "yes":
            merchantShop2()
        case "no":
            intro = f"You decided the man was too sketchy and continued on. . .\n"
            for character in intro:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.04)
            p.room += 1
            rooms()
def merchantShop2():
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
        "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
        "2 • Power Up Band (250 Gold)    4 • Quit\n"
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
    merchantShopTemp2()
def merchantShopTemp2():
    product1 = 200
    product2 = 250
    product3 = 200

    os.system('cls')
    shopUI4 = (
        "===================================================================\n"
        "                 What do you want to buy, traveller?               \n"
        "===================================================================\n"
        "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
        "2 • Power Up Band (250 Gold)                4 • Quit\n"
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
        "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
        "2 • Power Up Band (250 Gold)                4 • Quit\n"
        "===================================================================\n"
        f"Gold Amount: {p.gold} Gold\n\n\n"
        "Type the number of the item of your choice, or stop buying."
            )
        print(shopUI4)
        merchantChoice = int(input("‣ "))

    ### Items for shop ###
    match merchantChoice:
        case 1:
            ## Health Pot Up
            if p.gold < product1:
                print("Insufficient gold.")
                time.sleep(1)
                merchantShopTemp2()
            os.system('cls')
            shopUI4 = (
                "===================================================================\n"
                "                 What do you want to buy, traveller?               \n"
                "===================================================================\n"
                "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                "2 • Power Up Band (250 Gold)                4 • Quit\n"
                "===================================================================\n"
                f"Gold Amount: {p.gold} Gold\n\n\n"
                )
            print(shopUI4)
            choiceBuy = input("Buying Health Potion Upgrade: Confirm? (y or n): ")
            validChoice = ["y", "Y", "n", "N"]

            while choiceBuy not in validChoice:
                print("Invalid choice, try again.")
                time.sleep(1)
                os.system('cls')
                shopUI4 = (
                "===================================================================\n"
                "                 What do you want to buy, traveller?               \n"
                "===================================================================\n"
                "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                "2 • Power Up Band (250 Gold)                4 • Quit\n"
                "===================================================================\n"
                f"Gold Amount: {p.gold} Gold\n\n\n"
                )
                print(shopUI4)
                choiceBuy = input("Buying Health Potion Upgrade: Confirm? (Y or N): ")
            
            ## Yes or No
            if choiceBuy == "y" or choiceBuy == "Y":
                p.gold -= product1
                p.hpPotion += 2
                p.hpPotUp = True
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                    "2 • Power Up Band (250 Gold)                4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n\n"
                )
                print(shopUI4)
                print("You have upgraded your Health Potions, it now heals 50%!")
                time.sleep(0.25)
                print(f"You've gained 2 Health Potions. You now have {p.hpPotion} Health Potion/s!")
                time.sleep(0.25)
                input("Press Enter to continue.")
                merchantShopTemp2()
            if choiceBuy == "n" or choiceBuy == "N":
                merchantShopTemp2()
        case 2:
            ## Power Up Band
            if p.gold < product2:
                print("Insufficient gold.")
                time.sleep(1)
                merchantShopTemp2()
            os.system('cls')
            shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                    "2 • Power Up Band (250 Gold)                4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n\n"
                )
            print(shopUI4)
            choiceBuy = input("Buying Power Up Band: Confirm? (y or n): ")
            validChoice = ["y", "Y", "n", "N"]

            while choiceBuy not in validChoice:
                print("Invalid choice, try again.")
                time.sleep(1)
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                    "2 • Power Up Band (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n\n"
                )
                print(shopUI4)
                choiceBuy = input("Buying Power Up Necklace: Confirm? (Y or N): ")
            
            ## Yes or No
            if choiceBuy == "y" or choiceBuy == "Y":
                p.gold -= product2
                p.dmg += 4
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                    "2 • Power Up Band (250 Gold)                4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n\n"
                )
                print(shopUI4)
                print(f"Your DMG increased by 4!")
                input("Press Enter to continue.")
                merchantShopTemp2()
            if choiceBuy == "n" or choiceBuy == "N":
                merchantShopTemp2()
        case 3:
            ## HP Band
            if p.gold < product3:
                print("Insufficient gold.")
                time.sleep(1)
                merchantShopTemp2()
            os.system('cls')
            shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                    "2 • Power Up Band (250 Gold)                4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n\n"
                )
            print(shopUI4)
            print(shopUI4)
            choiceBuy = input("Buying HP Band: Confirm? (y or n): ")
            validChoice = ["y", "Y", "n", "N"]

            while choiceBuy not in validChoice:
                print("Invalid choice, try again.")
                time.sleep(1)
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                    "2 • Power Up Band (250 Gold)    4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n\n"
                )
                print(shopUI4)
                choiceBuy = input("Buying HP Band: Confirm? (Y or N): ")
            
            ## Yes or No
            if choiceBuy == "y" or choiceBuy == "Y":
                p.gold -= product3
                p.hp += 25
                p.hpMax += 25
                os.system('cls')
                shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                    "2 • Power Up Band (250 Gold)                4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n\n"
                )
                print(shopUI4)
                print(f"Your HP increased by 25!")
                input("Press Enter to continue.")
                merchantShopTemp2()
            if choiceBuy == "n" or choiceBuy == "N":
                merchantShopTemp2()
        case 4:
            ## Quit
            p.room += 1
            os.system('cls')
            shopUI4 = (
                    "===================================================================\n"
                    "                 What do you want to buy, traveller?               \n"
                    "===================================================================\n"
                    "1 • Health Potion Upgrade (200 Gold)        3 • HP Band (200 Gold)\n"
                    "2 • Power Up Band (250 Gold)                4 • Quit\n"
                    "===================================================================\n"
                    f"Gold Amount: {p.gold} Gold\n\n\n"
                )
            print(shopUI4)
            print(shopUI4)
            print("You decided to continue on your journey. . .")
            time.sleep(1)
            rooms()

def end():
    pass

####                         ####
#### ===== ROOM SETUPS ===== ####
####                         ####

## ROOM PICKER ##
def rooms():
    global player
    match p.room:
        case 0:
            room1()
        case 1:
            room2()
        case 2:
            merchant()
        case 3:
            player.hp = player.hpMax
            room3()
        case 4:
            player.hp = player.hpMax
            room4()
        case 5:
            merchant2()
        case 6:
            player.hp = player.hpMax
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
    time.sleep(1)
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
    time.sleep(1)
    os.system('cls')
    print("You healed to max HP!")
    time.sleep(1)
    os.system('cls')
    intro = f"You reach the outskirts of the castle. . .\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    enemySet1 = random.randint(1, 4)
    match enemySet1:
        case 1:
            enemy = spawn_enemy(knight, p.room)
        case 2:
            enemy = spawn_enemy(archer, p.room)
        case 3:
            enemy = spawn_enemy(assassin, p.room)
        case 4:
            enemy = spawn_enemy(wolf, p.room)
    os.system('cls')
    intro1 = f"You have encountered a/n {enemy.name}!"
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
    intro = f"You got inside the castle. . .\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    enemySet1 = random.randint(1, 3)
    match enemySet1:
        case 1:
            enemy = spawn_enemy(knight, p.room)
        case 2:
            enemy = spawn_enemy(archer, p.room)
        case 3:
            enemy = spawn_enemy(assassin, p.room)
    os.system('cls')
    intro1 = f"You have encountered a/n {enemy.name}!"
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
    global Enemy
    os.system('cls')
    intro = f"You reach the final room of the castle. . .\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    os.system('cls')
    enemy = spawn_enemy(dragon, p.room)
    intro = f"It's a Dragon! ! !\n"
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)

    time.sleep(1)
    os.system('cls')
    time.sleep(0.4)
    print(intro)
    time.sleep(0.4)
    os.system('cls')
    time.sleep(0.4)
    print(intro)
    time.sleep(0.4)
    os.system('cls')
    time.sleep(0.4)
    print(intro)
    time.sleep(0.4)

    bossBattleUI(enemy)

titleScreen()