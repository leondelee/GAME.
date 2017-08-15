import random
import time
from sys import exit
room=['Central Corridor','Laser Weapon Armory','Bridge Room','Escape Pod']
class Map:
    def start(self):
        print("Welcome to Gothons from Planet Percal.You are in a central corridor of an old house in an strange palnet.And you  meet Gothon...")
        print("Gothon:\"You!There!I\'m Gonthon,you won\'t leave this room alive until you tell me a joke!\"")
        print("Your choices:\nA.Tell him a really funny joke.\nB.I only tell jokes to my gilrfriend.")
        c=input("Please choose...")
        if c=='A':
            print("Leon:\"joke\"")
            print("Gothon:\"You funny bastard hhhhh,I\'m laughing to death!Fine,choose a room to continue.\"")
            print("Your choices:\nA.%s\nB.%s\nC.%s"%(room[1],room[2],room[3]))
            c=input()
            if c=='A':
                self.next_scene('LaserWeaponArmory')
            elif c=='B':
                self.next_scene('Bridge')
            elif c=='C':
                self.next_scene('EscapePod')
            else:
                print("Fxxk you!\nGo away and enter a random room!")
                d=random.randint(1,3)
                if d==1:
                    self.next_scene('LaserWeaponArmory')
                elif d==2:
                    self.next_scene('Bridge')
                elif d==3:
                    self.next_scene('EscapePod')
        elif c=='B':
            de.enter('Ce')
    def next_scene(self,scene_name):
        if scene_name=='LaserWeaponArmory':
            self.opening_scene('LaserWeaponArmory')
            La.enter()
        elif scene_name=='Bridge':
            self.opening_scene('Bridge')
            Br.enter()
        elif scene_name=='EscapePod':
            self.opening_scene('EscapePod')
            Es.enter()
    def opening_scene(self,room_name):
        print("Entering %s..."%room_name)
        time.sleep(2)
class Scene:
    pass
class Death(Scene):
    def over(self):
        print("Game over!")
    def enter(self,scenename):
        if scenename=='Ce':
            print("Gothon has taken your mind to steal some jokes in it.")
            self.over()
            exit(0)
        elif scenename=='La':
            print("Booooooooooooooooooooooom!")
            self.over()
            exit(0)
        elif scenename=='Br':
            print("Fishs say:\"Tasty!\"")
            self.over()
            exit(0)
        elif scenename=='Es':
            print("You can\'t escape .")
            self.over()
            exit(0)
class CentralCorridor(Scene):
    def enter(self):
        pass
class LaserWeaponArmory(Scene):
    def __init__(self):
        self.flag=False
    def enter(self):
        print("Congratulations!You have a chance to get a laser weapon.But you have to answer a question.What\'s the main material of atom bomb?\nA.C\nB.Fe\nC.U")
        e=input()
        if e=='C':
            self.flag=True
            print("You have got the laser weapon,make a choice to continue:\nA.Bridge\nB.Escape Pod")
            f=input()
            if f=='A':
                a_map.next_scene('Bridge')
            elif f=='B':
                a_map.next_scene('EscapePod')
        else:
            de.enter('La')
class Bridge(Scene):
    def __init__(self):
        self.flag=False
    def enter(self):
        if La.flag:
            print("You meet the final boss GSL,take your laser weapon to kill it!")
            print("-"*10)
            print("Nuclear weapon ready.")
            time.sleep(1)
            print(5)
            time.sleep(1)
            print(4)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            print("You win!And you can go to the escape pod now!")
            self.flag=True
            a_map.next_scene('EscapePod')
        else:
            print("You have no weapon,why are you here?")
            de.enter('Br')
class EscapePod(Scene):
    def enter(self):
        if Br.flag:
            print("Bravo!Here you come to the last stage!But there are 3 rooms,guess which one is the escape pod?")
            print("I\'m so kind that I can give you a prompt:the right number is deux.")
            g=input()
            if g == '2':
                print("Bingo!You have returned home ,safe and sound!")
                exit(0)
            else:
                print("Sadly,you have a wrong choice")
                a_map.next_scene('Es')
        else:
            print("LGS has you!And you have become one of his hair!")
            de.enter('Es')
de=Death()
La=LaserWeaponArmory()
Br=Bridge()
Es=EscapePod()
a_map=Map()
a_map.start()

