import cmd
import textwrap
import sys
import os
import time
import random
import copy

os.system('cls')
class player:
    ## == Your Character == ##
    def __init__(self):
        self.name = "Player"
        self.hp = 120
        self.hpMax = 120
        self.mp = 20
        self.dmg = 5
        self.critC = 0.5
        self.critM = 2.25
        self.dodge = 0.5
        self.role = ""
        self.wep = "Fists"
        self.gold = 300
        self.hpPotion = 3
        self.room = 0
p = player()

class Enemy:
    def __init__(self, name, hp, dmg, critC, critM, dodge):
        self.name = name
        self.hp = hp
        self.hpMax = hp
        self.dmg = dmg
        self.critC = critC
        self.critM = critM
        self.dodge = dodge



def gameOver():
    os.system('cls')
    gameOverText = "G A M E   O V E R . . ."
    for char in gameOverText:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)
    input("\n\nPress Enter to go back to the menu.")
    battleUI()

## == Attack Choice == ##
def atkchoice():
    # Player attack
    if random.random() < Enemy.dodge:
        os.system('cls')
        fightUI1 = (
                "========================================\n"
                f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
                f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
                "========================================\n"
                )
        fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Item               4 • Defend\n"
                )
        print(fightUI1)
        print(fightUI2)
        print("You missed!")
    else:
        isCrit = random.random() < myPlayer.critC
        finalDMGplayer = myPlayer.dmg

        if isCrit:
            finalDMGplayer = myPlayer.dmg * myPlayer.critM
            os.system('cls')
            fightUI1 = (
                "========================================\n"
                f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
                f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
                "========================================\n"
                    )
            fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Item               4 • Defend\n"
                    )
            crit = "You've dealt a CRITICAL HIT!!"
            print(fightUI1)
            print(fightUI2)
            print(crit)
            time.sleep(1)

        ### finaldmg
        Enemy.hp -= finalDMGplayer
        if Enemy.hp <= 0:
            Enemy.hp = 0
            print(f"You have dealt {finalDMGplayer}!")
            time.sleep(1)
            os.system('cls')
            fightUI1 = (
                "========================================\n"
                f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
                f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
                "========================================\n"
                    )
            fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Item               4 • Defend\n"
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
            f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
            f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
            "========================================\n"
            )
        fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Item               4 • Defend\n"
                )
        print(fightUI1)
        print(fightUI2)
        print(f"You have dealt {finalDMGplayer}!")

    time.sleep(2)

    # Enemy attack (only if alive)
    if Enemy.hp > 0:
        if random.random() < myPlayer.dodge:
            os.system('cls')
            fightUI1 = (
                "========================================\n"
                f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
                f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
                "========================================\n"
                )
            fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Item               4 • Defend\n"
                )
            print(fightUI1)
            print(fightUI2)
            print(f"The {Enemy.name} missed!")
        else:
            isCrit = random.random() < Enemy.critC
            finalDMGenemy = Enemy.dmg

            if isCrit:
                finalDMGenemy = Enemy.dmg * Enemy.critM
                os.system('cls')
                fightUI1 = (
                    "========================================\n"
                    f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
                    f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
                    "========================================\n"
                    )
                fightUI2 = (
                    "1 • Attack             3 • Inspect\n"
                    "2 • Item               4 • Defend\n"
                    )
                print(fightUI1)
                print(fightUI2)
                print(f"\nThe {Enemy.name} hit a CRITICAL HIT!!")
                time.sleep(1)
            
            ### finaldmg
            myPlayer.hp -= finalDMGenemy
            if myPlayer.hp <= 0:
                myPlayer.hp = 0
                print(f"The {Enemy.name} has dealt {Enemy.dmg}!")
                time.sleep(0.5)
                gameOver()
            os.system('cls')
            fightUI1 = (
                "========================================\n"
                f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
                f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
                "========================================\n"
                    )
            fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Item               4 • Defend\n"
                    )
            print(fightUI1)
            print(fightUI2)    
            print(f"The {Enemy.name} has dealt {Enemy.dmg}!")
        time.sleep(0.5)
        input("\nPress Enter to continue.")
    battleUItemp()

def battleUItemp():
    while Enemy.hp > 0 and myPlayer.hp > 0:
        os.system('cls')
        fightUI1 = (
            "========================================\n"
            f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
            f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
            "========================================\n"
            )
        fightUI2 = (
                "1 • Attack             3 • Inspect\n"
                "2 • Item               4 • Defend\n"
                )
        print(fightUI1)
        print(fightUI2)
        
        try:
            choice = int(input("What do you want to do?: "))
            if choice == 1:
               atkchoice()
            if choice == 2:
                pass
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

def event():
    
    while Enemy.hp > 0 and myPlayer.hp > 0:
        print(f"{myPlayer.name} HP: {myPlayer.hp}/{myPlayer.hpMax}")
        print(f"{Enemy.name} HP: {Enemy.hp}/{Enemy.hpMax}")
        try:
            dmg = int(input("Type the DMG: "))
        except ValueError:
            os.system('cls')
            event()
        Enemy.hp -= dmg
        
        if Enemy.hp < 0:
            Enemy.hp = 0

        if Enemy.hp > 0:
            myPlayer.hp -= Enemy.dmg

        if myPlayer.hp < 0:
            myPlayer.hp = 0
        os.system('cls')


def battleUI():
    os.system('cls')
    fightUI1 = (
        "========================================\n"
        f"{myPlayer.name}: {myPlayer.hp}/{myPlayer.hpMax}\n"
        f"{Enemy.name}: {Enemy.hp}/{Enemy.hpMax}\n"
        "========================================\n"
            )

    for char in fightUI1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

    fightUI2 = (
            "1 • Attack             3 • Inspect\n"
            "2 • Item               4 • Defend\n"
            )

    for char in fightUI2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
    battleUItemp()

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
def merchant():
    p.room +=1
    rooms()
###                          ###
### TESTING SCALING ENEMY HP ###
###                          ###
def titleTEMP():
    print("Title Screen")
    input("Enter to continue.")
    rooms()

## ENEMY STAT SHEET ##
def goblin():
    return Enemy("Goblin", 25, 8, 0.05, 1.25, 0.05)
def kobold():
    return Enemy("Kobold", 20, 10, 0.15, 1.25, 0.05 )
def bandit():
    return Enemy("Bandit", 30, 8, 0.20, 1.5, 0.10)
def boar():
    return Enemy("Boar", 50, 5, 0.05, 1.25, 0.05)

## ENEMY SCALING ##
def spawn_enemy(template_func, room):
    e = template_func()   # new Enemy

    scale = 1 + room * 0.50

    e.hp = int(e.hp * scale)
    e.hpMax = e.hp
    e.dmg = int(e.dmg * scale)

    return e

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

## ROOMS LIST ##
def room1():
    global Enemy

    os.system('cls')
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
    print(f"Enemy Name: {enemy.name}")
    print(f"Enemy HP: {enemy.hp}/{enemy.hpMax}")
    print(f"Enemy DMG spread: {enemy.dmg}, {enemy.dmg}, {enemy.dmg}, {enemy.dmg}\n")

    results = []
    p.dmg = 3
    
    for _ in range(20):
        finalDMG = random.randint(p.dmg - 1, p.dmg + 3)
        results.append(finalDMG)

    p.hpMax += 20
    p.hpMax *= 1.15
    p.hpMax = round(p.hpMax, 2)

    print(p.hpMax)
    print(results)
    time.sleep(1)
    input("Enter to continue.")
    p.room += 1
    rooms()
def room2():
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
    print(f"Enemy Name: {enemy.name}")
    print(f"Enemy HP: {enemy.hp}/{enemy.hpMax}")
    print(f"Enemy DMG spread: {enemy.dmg}, {enemy.dmg}, {enemy.dmg}, {enemy.dmg}\n")
    time.sleep(1)
    input("Enter to continue.")
    p.room += 1
    rooms()
def room3():
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
    print(f"Enemy Name: {enemy.name}")
    print(f"Enemy HP: {enemy.hp}/{enemy.hpMax}")
    print(f"Enemy DMG spread: {enemy.dmg}, {enemy.dmg}, {enemy.dmg}, {enemy.dmg}\n")
    time.sleep(1)
    input("Enter to continue.")
    p.room += 1
    rooms()
def room4():
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
    print(f"Enemy Name: {enemy.name}")
    print(f"Enemy HP: {enemy.hp}/{enemy.hpMax}")
    print(f"Enemy DMG spread: {enemy.dmg}, {enemy.dmg}, {enemy.dmg}, {enemy.dmg}\n")
    time.sleep(1)
    input("Enter to continue.")
    p.room += 1
    rooms()
def boss():
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
    print(f"Enemy Name: {enemy.name}")
    print(f"Enemy HP: {enemy.hp}/{enemy.hpMax}")
    print(f"Enemy DMG spread: {enemy.dmg}, {enemy.dmg}, {enemy.dmg}, {enemy.dmg}\n")
    time.sleep(1)
    input("Enter to continue.")
    p.room += 1
    rooms()
def end():
    pass

titleTEMP()
os.system('cls')