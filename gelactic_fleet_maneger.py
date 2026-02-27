import time

class spaceship:
    def __init__(self, name , nfule, wfule , fbr, norm_dist, warp_dist,):
        self.name = name
        self.nfule = nfule
        self.wfule = wfule
        self.fbr = fbr
        self.norm_dist = norm_dist
        self.warp_dist = warp_dist
    def travel_norm(self):
        print("traveling")
        self.nfule = self.nfule - (self.fbr * self.norm_dist)
        return print(f"{self.nfule} units of normal fule remaneing")
    def travel_warp(self):
        self.wfule = self.wfule -(self.fbr * self.warp_dist)
        return print(f"{self.wfule} units of warp fule remaneing")
    def sustain_damege(self):
        print("takeing damege")

class fighter(spaceship):
    def __init__(self, name, nfule, wfule, fbr, norm_dist, warp_dist, damege):
        super().__init__(name, nfule, wfule, fbr, norm_dist, warp_dist,)
        self.damege = damege
    def attack(self):
        target = input("Entre your target: ")
        print("Attacking...")
        time.sleep(1.5)
        print(f"{target} has sustaind {self.damege} damege")

class transport(spaceship):
    def __init__(self, name, nfule, wfule, fbr, norm_dist, warp_dist, cargo):
        super().__init__(name, nfule, wfule, fbr, norm_dist, warp_dist)
        self.cargo = cargo # expecting a list
    def deliver_cargo(self):
        if not self.cargo:
            print("no cargo to deliver")
        else:
            print("delivering ", self.cargo[0])
            self.cargo.pop(0)
    def recive_cargo(self):
        new_cargo = input("Entre what you want to add to your cargo: ")
        print(F"{new_cargo} added to your cargo.")
        self.cargo.append(new_cargo)

xf355 = fighter("bigg bessy", 1000, 200, 1.5, 100, 4, 50)
xf355.attack()