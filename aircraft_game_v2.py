'''
aircraft game
26-1-26
v2
Andrew Cowie
'''

class plane:
    def __init__(self, doors):
        self.doors = doors
    def fly(self):
        print ("plane is flying")

class mill(plane):
    def __init__(self, doors, bombs):
        super().__init__(doors)
        self.bombs = bombs
    def defend(self):
        print("defending")

class jet(mill):
    def __init__(self, doors, bombs, ab):
        super().__init__(doors, bombs)
        self.doors = doors
        self.bombs = bombs
        self.ab = ab
    def drop_bombs(self):
        print("dropping", self.bombs)
    def shoot(self):
        print("firing")

class cargo(mill):
    def __init__(self, doors, bombs, max_wegit, cargo):
        super().__init__(doors, bombs)
        self.doors = doors
        self.bombs = bombs
        self.max_wegit = max_wegit
        self.cargo = cargo
    def air_drop(self):
        print("dropping ", self.cargo)
    def para_drop(self):
        print("releaseing paras")

class civ(plane):
    def __init__(self, doors, pax, speed):
        super().__init__(doors)
        self.doors = doors
        self.pax = pax
        self.speed = speed
    def flt_pln(self, input("entre your starting airport code eg. EGOD: "), input("Entre your denstanation airport code eg. EGOD :")):
        print("boarding ", self.pax," pasengers")
        

class comercial(civ):
    def __init__(self, doors, pax, speed, engin_type):
        super().__init__(doors, pax, speed)
        self.doors = doors
        self.pax = pax
        self.speed = speed
        self.engin_type = engin_type
    def board_pax(self):
        print("boarding pasengers")
        
class priv(civ):
    def __init__(self, doors, pax, speed, rang):
        super().__init__(doors, pax, speed)
        self.doors = doors
        self.pax = pax
        self.speed = speed
        self.rang = rang
    def vfr(self):
        print("you are now in Visual flight rules")
    def ifr(self):
        print("you are now in instrament flight rules")