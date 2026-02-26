'''
oop inheritance plane
11-12-2025
Andy Cowie
'''

class plane:  # grandparent class plane
    def __init__(self, name, wing_type, num_doors):
        self.name = name
        self.wing_type = wing_type
        self.num_doors = num_doors
    def show_info():
        print(f"{wing_type} wings, {num_doors} doors") 

class mill(plane): # mill is child of plane
    def __init__(self, name, wing_type, num_doors, wepons):
        super().__init__(name, wing_type, num_doors)
        self.wepons = wepons

class fighter(mill): # fighter is child of mill and mill is child of plane
    def __init__(self, name, wing_type, num_doors, wepons, bombs):
        super().__init__(name, wing_type, num_doors, wepons)
        self.bombs = bombs
    def attack(self):
        print(f"{self.name} is attacking with {self.bombs}")
    
class cargo(mill):  # cargo is child of mill and mill is child of plane
    def __init__(self, name, wing_type, num_doors, wepons, load):
        super().__init__(name, wing_type, num_doors, wepons)
        self.load = load
    def air_drop(self):
        print(f"{self.name} is dropping {self.load}")

class civ(plane): # civ is child of plane
    def __init__(self, name, wing_type, num_doors, pax):
        super().__init__(name, wing_type, num_doors)
        self.pax = pax

class short(civ):   # short is child of civ and civ is child of plane
    def __init__(self, name, wing_type, num_doors, pax, dist):
        super().__init__(name, wing_type, num_doors, pax)
        self.dist = dist
    def short_fly(self):