import sys
import os
import random
import pickle
import time


weapons = {"Great Sword": 40,
                    "Massive Sword": 100}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.maxmp = 100
        self.mp = self.maxmp
        self.base_attack = 0
        self.gold = 100
        self.Class = None
        self.lv = 1
        self.curexp =0
        self.maxexp = 20
        self.healthPotions = 0
        self.mpPotions = 0
        self.weap = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]


    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 5

        if self.curweap == "Great Sword":
                attack += 15

        if self.curweap == "Massive Sword":
            attack += 30

        return attack

class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.maxmp = 100
        self.mp = self.maxmp
        self.attack = 5
        self.goldgain = 10
        self.expgain = 5
GoblinIG = Goblin("Goblin")



class Thief:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.maxmp = 70
        self.mp = self.maxmp
        self.attack = 7
        self.goldgain = 15
        self.expgain  =10
ThiefIG = Thief("Thief")



def main():
    os.system("cls")
    print("Welcome to the game\n")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
    option = input("--> ")
    if option == "1":
        start()

    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system("cls")
            with open("savefile", "rb") as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Save loaded")
            option = input(" ")
            start1()
        else:
            print("You have no save file for this game.")
            option = input(" ")
            main()

    elif option == "3":
        sys.exit()

    else:
        main()



def start():
    os.system("cls")
    option = input("What is your name? ")
    global PlayerIG
    PlayerIG = Player(option)
    chooseClass()
    start1()



def lvup():
    if PlayerIG.curexp == PlayerIG.maxexp:
        os.system("cls")
        print("You have leveled up")
        print("Choose what stat to level")
        print("1.) Damage")
        print("2.) HP")
        print("3.) MP")

        option = input("--> ")

        if PlayerIG.Class == "Warrior":
            if option == "1":
                os.system("cls")
                print("Damage increased")
                PlayerIG.base_attack  += 5
                option = input(" ")
                PlayerIG.maxexp *= 2

            elif option == "2":
                os.system("cls")
                print("Hp increased")
                PlayerIG.maxhealth += 15
                option = input(" ")
                PlayerIG.maxexp *= 2

            elif option == "3":
                os.system("cls")
                print("MP increased")
                PlayerIG.maxmp += 5
                option = input(" ")
                PlayerIG.maxexp *= 2

            else:
                lvup()

        if PlayerIG.Class == "Mage":
            if option == "1":
                os.system("cls")
                print("Damage increased")
                PlayerIG.base_attack  += 5
                option = input(" ")
                PlayerIG.maxexp *= 2

            elif option == "2":
                os.system("cls")
                print("Hp increased")
                PlayerIG.maxhealth += 10
                option = input(" ")
                PlayerIG.maxexp *= 2

            elif option == "3":
                os.system("cls")
                print("MP increased")
                PlayerIG.maxmp += 15
                option = input(" ")
                PlayerIG.maxexp *= 2

            else:
                lvup()

        if PlayerIG.Class == "Assasin":
            if option == "1":
                os.system("cls")
                print("Damage increased")
                PlayerIG.base_attack  += 15
                option = input(" ")
                PlayerIG.maxexp *= 2

            elif option == "2":
                os.system("cls")
                print("Hp increased")
                PlayerIG.maxhealth += 10
                option = input(" ")
                PlayerIG.maxexp *= 2

            elif option == "3":
                os.system("cls")
                print("MP increased")
                PlayerIG.maxmp += 5
                option = input(" ")
                PlayerIG.maxexp *= 2

            else:
                lvup()

            PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.mp = PlayerIG.maxmp

    else:
        pass



def chooseClass():
    print("Choose your class")
    print("1.) Warrior")
    print("2.) Mage")
    print("3.) Assasin")

    option = input("--> ")

    if option == "1":
        PlayerIG.Class = "Warrior"
        PlayerIG.maxhealth = 150
        PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.maxmp = 50
        PlayerIG.mp = PlayerIG.maxmp
        PlayerIG.base_attack = 5

    elif option == "2":
        PlayerIG.Class = "Mage"
        PlayerIG.maxhealth = 75
        PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.maxmp = 200
        PlayerIG.mp = PlayerIG.maxmp
        PlayerIG.base_attack = 5

    elif option == "3":
        PlayerIG.Class = "Assasin"
        PlayerIG.maxhealth = 100
        PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.maxmp = 100
        PlayerIG.mp = PlayerIG.maxmp
        PlayerIG.base_attack = 10

    else:
        chooseClass()



def start1():
    os.system("cls")
    print("Name:",PlayerIG.name)
    print("HP:",PlayerIG.health,"/",PlayerIG.maxhealth)
    print("MP:",PlayerIG.mp,"/",PlayerIG.maxmp)
    print("Class:",PlayerIG.Class)
    print("LV",PlayerIG.lv)
    print("EXP",PlayerIG.curexp,"/",PlayerIG.maxexp)
    print("Current Weapons:",PlayerIG.curweap)
    print("Attack",PlayerIG.attack)
    print("Gold",PlayerIG.gold)
    print("HP Potions",PlayerIG.healthPotions)
    print("MP Potions",PlayerIG.mpPotions)

    print("1.) Look at the map")
    print("2.) Store")
    print("3.) Save")
    print("4.) Fight")
    print("5.) Exit")
    print("6.) Inventory")
    print("7.) Tavern")

    option = input("--> ")
    if option == "1":
        map()

    elif option == "2":
        store()

    elif option == "3":
        os.system("cls")
        with open("savefile", "wb") as f:
            pickle.dump(PlayerIG, f)
            print("\nGame has been saved\n")
        option = input(" ")
        start1()

    elif option == "4":
        prefight()

    elif option == "5":
        sys.exit()

    elif option == "6":
        inventory()

    elif option == "7":
        tavern()

    else:
        start1()



def tavern():
    os.system("cls")
    print("\nHello Welcome to the Tavern\n")
    print("1.) Talk to the bartender")
    print("2.) Rest")
    print("3.) Exit")
    option = input("--> ")

    if option == "1":
        bartender()

    elif option == "2":
        rest()

    elif option == "3":
        start1()

    else:
        tavern()



def rest():
    os.system("cls")
    if PlayerIG.gold <= 25:
        PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.mp = PlayerIG.maxexp
        print("You feel well rested")

        option = input(" ")

        tavern()

    else:
        print("You don't have enough gold")

        option = input(" ")

        tavern()



def bartender():
    os.system("cls")
    print("Hello there what would you like?")
    print("1.) Buy Potions")
    print("2.) Ask about quests(NOT WORKING)")
    print("3.) Exit")

    option = input("--> ")

    if option == "1":
        os.system("cls")
        print("1.) Buy HP Potions")
        print("2.) Buy MP Potions")

        option = input("--> ")

        if option == "1":
            buyHPpotion()

        elif option == "2":
            buyMPpotion()

        else:
            print("Thats not on sale")

    elif option == "2":
        quests()

    elif option == "3":
        tavern()

    else:
        bartender()



def buyHPpotion():
    os.system("cls")
    if PlayerIG.gold <= 50:
        PlayerIG.healthPotions += 1
        print("You have bought an HP Potion")

        option = input(" ")

        bartender()

    else:
        print("You don't have enough gold")

        option = input(" ")

        bartender()



def buyMPpotion():
    os.system("cls")
    if PlayerIG.gold <= 50:
        PlayerIG.mpPotions += 1
        print("You have bought an MP Potion")

        option = input(" ")

        bartender()

    else:
        print("You don't have enough gold")

        option = input(" ")

        bartender()



def equip():
    os.system("cls")
    print("What do you want to equip?")
    for weapon in PlayerIG.weap:
        print(weapon)
    print("1.) To go back")
    option = input("--> ")
    if option == PlayerIG.curweap:
        print("You already have that weapon equipped")
        option = input(" ")
        equip()

    elif option == "1":
        inventory()

    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print("You have equipped",option)
        option = input(" ")
        equip()

    else:
        print("You don't have",option,"in your inventory")
        equip()



def inventory():
    os.system("cls")
    print("What do you want to do?")
    print("1.) Equip Weapon")
    print("2.) Go back")
    option = input("--> ")

    if option == "1":
        equip()
    elif option == "2":
        start1()



def prefight():
    global enemy
    enemynum = random.randint(1, 2)

    if enemynum == 1:
        enemy = GoblinIG

    else:
        enemy = ThiefIG

    fight()



def fight():
    os.system("cls")

    print(PlayerIG.name,"       VS      ",enemy.name)
    print("Player HP:",PlayerIG.health,"/",PlayerIG.maxhealth,"              ",enemy.name,"HP:",enemy.health,"/",enemy.maxhealth)
    print("HP Potions:", PlayerIG.healthPotions, "MP Potions:",PlayerIG.mpPotions)
    print("1.) Attack")
    print("2.) Drink an HP Potion")
    print("3.) Drink an MP Potion")
    print("4.) Run")
    option = input("-->")
    if option == "1":
        attack()

    elif option == "2":
        drinkHPPotion()

    elif option == "3":
        drinkMPPotion()

    elif option == "4":
        run()
    else:
        fight()



def attack():
    os.system("cls")

    option = input(" ")
    enemy.health -= PlayerIG.attack
    print("You deal",PlayerIG.attack,"damage")
    option = input(" ")
    os.system("cls")

    if enemy.health <= 0:
        PlayerIG.gold += enemy.goldgain
        PlayerIG.curexp += enemy.expgain
        print("You have gained",enemy.expgain,"XP")

        option = input(" ")

        lvup()
        win()

    PlayerIG.health -= enemy.attack
    print("The enemy deals",enemy.attack,"damage!")
    option = input(" ")

    if PlayerIG.health <= 0:
        dead()

    else:
        fight()



def drinkHPPotion():
    os.system("cls")

    if PlayerIG.healthPotions == 0:
        print("You don't have any HP potions")

    else:
        PlayerIG.healthPotions += 50
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print("You drank a potion")

        option = input(" ")
        fight()



def drinkMPPotion():
    os.system("cls")

    if PlayerIG.mpPotions == 0:
        print("You don't have any MP potions")

    else:
        PlayerIG.mpPotions += 50
        if PlayerIG.mp > PlayerIG.maxmp:
            PlayerIG.mp = PlayerIG.maxmp
            print("You drank a potion")

    option = input(" ")
    fight()



def run():
    os.system("cls")
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You have gotten away!")
        option = input(" ")
        start1()
    else:
        print("You failed to get away!")
        option = input(" ")
        os.system("cls")

        PlayerIG.health -= enemy.attack
        print("The enemy deals",enemy.attack,"damage!")
        option = input(" ")
        if PlayerIG.health <= 0:
            dead()

        else:
            fight()



def win():
    os.system("cls")
    enemy.health = enemy.maxhealth
    print("You have defeated the",enemy.name)
    print("You found",enemy.goldgain,"gold")
    option = input(" ")
    start1()



def dead():
    os.system("cls")
    print("You have died")
    option = input(" ")
    sys.exit()



def store():
    os.system("cls")
    print("Welcome to the shop")
    print("\nWhat would you like to buy?\n")
    print("Great Sword (40 Gold)")
    print("Massive Sword (100 Gold)")
    print("Back")
    option = input(" ")

    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            os.system("cls")
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print("You have bought",option)
            option = input(" ")
            store()

        else:
            os.system("cls")
            print("You don't have enough gold")
            option = input(" ")
            store()

    elif option == "back" or "Back":
        start1()

    else:
        os.system("cls")
        print("That item does not exist")
        option = input(" ")
        store()



main()
