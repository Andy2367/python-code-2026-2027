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
        
