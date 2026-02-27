import time
import random as rand
class spaceship:
    def __init__(self, name , nfule, wfule , fbr, norm_dist, warp_dist):
        self.name = name
        self.nfule = nfule
        self.wfule = wfule
        self.fbr = fbr
        self.norm_dist = norm_dist
        self.warp_dist = warp_dist
    def travel_norm(self):
        print("traveling")
        self.nfule = self.nfule - (self.fbr * self.norm_dist)
        return print(f"{self.nfule} units of normal fule remaneing.")
    def travel_warp(self):
        dist = float(input("how far do you want to go in lightyears? e.g. 2.5"))
        self.warp_dist = dist
        self.wfule = self.wfule -(self.fbr * self.warp_dist)
        return print(f"{self.wfule} units of warp fule remaneing.")

class fighter(spaceship):
    def __init__(self, name, nfule, wfule, fbr, norm_dist, warp_dist, kills):
        super().__init__(name, nfule, wfule, fbr, norm_dist, warp_dist)
        self.kills = kills
    def attack(self):
        target = input("What do you want to attack? e.g cx2213-alpha.")
        print("Attaking target...")
        time.sleep(1)
        print(f"{target} was destroyed.")
        self.kills = self.kills + 1

class corvet(spaceship):
    def __init__(self, name, nfule, wfule, fbr, norm_dist, warp_dist, cargo, crew):
        super().__init__(name, nfule, wfule, fbr, norm_dist, warp_dist)
        self.cargo = cargo
        self.crew = crew
    def load(self):
        cargo = input("what do you want to load in to the cargo-bay? ")
        print("loading cargo...")
        time.sleep(1.5)
        print(f"{cargo} was loades sucsefuly.")

class transport(spaceship):
    def __init__(self, name, nfule, wfule, fbr, norm_dist, warp_dist, pax):
        super().__init__(name, nfule, wfule, fbr, norm_dist, warp_dist)
        self.pax = pax
    def board_pax(self):
        pax = int(input("how many pasengers do you want to board?"))
        print("boarding pasengers...")
        self.pax = self.pax + pax
        time.sleep(2)
        print("all pasengers are aboard.")

class science(spaceship):
    def __init__(self, name, nfule, wfule, fbr, norm_dist, warp_dist, task):
        super().__init__(name, nfule, wfule, fbr, norm_dist, warp_dist)
        self.task = task
    def reaserch(self):
        task = input("what do you want to reasurch? e.g. nebula.")
        print(f"traveling to reaserch sight...")
        time.sleep(1.3)
        print("arived at reasurch location, begining scans...")
        time.sleep(1)
        print("reasurch complete")
        print("data added to archives")

def create_fighter():
    name = input("input the name of the fighter. e.g. sf109-bravo")
    nfule = input("input the amount of normal fule")
    wfule = input("input the amount of warp fule")
    fbr = rand.randint(5, 10)
    normd = 0
    warpd = 0
    kills = 0
    ship = fighter(name, nfule, wfule, fbr, normd, warpd, kills)

def create_corvet():
    name = input("input the name of the fighter. e.g. sc011-oscar")
    nfule = input("input the amount of normal fule")
    wfule = input("input the amount of warp fule")
    fbr = rand.randint(3, 7)
    normd = 0
    warpd = 0
    cargo = "No cargo"
    crew = int(input("pick a crew size from 2-6"))
    if crew <2 or crew >6:
        print("invalid input you must input an integer between 2 and 6")
    else:
        pass
    ship = corvet(name, nfule, wfule, fbr, normd, warpd, cargo, crew)

def create_transport():
    name = input("input the name of the fighter. e.g. st209-yanky")
    nfule = input("input the amount of normal fule")
    wfule = input("input the amount of warp fule")
    fbr = rand.randint(1, 5)
    normd = 0
    warpd = 0
    pax = 0
    ship = transport(name, nfule, wfule, fbr, normd, warpd, pax)

def create():
    print("what type of ship do you want to make? ")
    print("1. fighter. quick & agile but a real gas guseler")
    print("2. transport. very eficiant but slow and defenceless")
    print("3. corvet. a hybrid of the other two with plenty of defenses but able to carry cargo and people, faster and more nimble than the transport but les fule eficiant")
    inp = int(input())
    if inp < 1 or inp > 3:
        print("invalid input pleas enter either 1, 2 of 3")
        create()
    else:
        if inp == 1:
            create_fighter()
        elif inp == 2:
            create_transport()
        elif inp == 3:
            create_corvet()