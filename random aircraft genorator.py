import time
import random

class plane:
    def __init__(self, doors, in_air, on_runway, power):
        self.doors = doors
        self.in_air = in_air
        self.on_runway = on_runway
        self.power = power
    def fly(self):
        print ("plane is flying")
        self.in_air = True
    def get_info(self):
        print(self.doors," doors")
    def taxi(self):
        self.on_runway == True
        print("on runway")
    def startup(self):
        self.power = True
        print("Plane is runing")
    def shutdown(self):
        self.power = False
        print("plane has been turned off")
    def land(self):
        self.in_air = False
        print("plane has landed")

class mill(plane):
    def __init__(self, doors, in_air, on_runway, power, bombs):
        super().__init__(doors, in_air, on_runway, power)
        self.bombs = bombs
    def defend(self):
        print("defending")
    def get_info(self):
        print(self.doors, " doors ", self.bombs, "bombs")

class jet(mill):
    def __init__(self, doors, in_air, on_runway, power, bombs, ab):
        super().__init__(doors, in_air, on_runway, power, bombs)
        self.ab = ab
    def drop_bombs(self):
        print("dropping", self.bombs)
    def shoot(self):
        print("firing")
    def get_info(self):
        if self.ab == True:
            print(self.doors," doors, has ", self.bombs," bombs, has after-burner")
        elif self.ab != True:
            print(self.doors," doors, has ", self.bombs," bombs, doesn't has after-burner")

class cargo(mill):
    def __init__(self, doors, in_air, on_runway, power, bombs, max_wegit, cargo):
        super().__init__(doors, in_air, on_runway, power, bombs)
        self.max_wegit = max_wegit
        self.cargo = cargo
    def air_drop(self):
        print("dropping ", self.cargo)
    def para_drop(self):
        print("releaseing paras")
    def get_info(self):
        print(self.doors," doors, ", self.bombs," bombs, ", self.max_wegit," kg max load, ", self.cargo," in cargo bay")

class civ(plane):
    def __init__(self, doors, in_air, on_runway, power, pax, speed):
        super().__init__(doors, in_air, on_runway, power)
        self.pax = pax
        self.speed = speed
    def flt_pln(self, start, end):
        print("Calculateing flight plan from ", start," to ", end)
        time.sleep(1.5)
        print("Flight plan confermed")
    def board(self):
        print("Boarding ", self.pax," pasengers")
    def get_info(self):
        print(self.doors," doors, ", self.pax," pasengers, ", self.speed," kts max speed")


planes = []
try:
    while True:
        print("what would you like to do")
        print("1 to add a palne")
        print("2 to see your planes")
        print("3. use a plane")
        inp = input()

        if inp == "1":
            name = input("Enter the name of your aircraft: ")
            for i in range(len(planes)):
                if planes[i] == name:
                    print("sorry you can't haev the same name twice")
                else:
                    print()
                    print("1 for fighter")
                    print("2 for mill transport")
                    print("3 for civ plane")
                    print("4 to quit")
                    print()
                    a_type = input()
                    accept_type = ("1","2","3","4","5","6")
                    if a_type not in accept_type:
                        print("sorry this input is not acceptable. pleas try again")

                    elif a_type == "3":
                        plane_ = civ(random.randint(1,8), random.randint(2,500), random.randint(90,350))
                        planes.append(name)
                        planes.append(plane_)
                        print(f"{name} added to my planes")

                    elif a_type == "2":
                        cg = ["Helecopter","suply drop","armored transport","paratroops"]
                        cgo = cg[random.randint(0, 2)]
                        plane_ = cargo(random.randint(2,8), random.randint(0,25), random.randint(200, 85000), cgo)
                        planes.append(name)
                        planes.append(plane_)
                        print(f"{name} added to my planes")

                    elif a_type == "1":
                        bm = ["paveway-4", "aim 9", "pikle"]
                        bms = bm[random.randint(0,2)]
                        abn = [True, False]
                        aburn = abn[random.randint(0,1)]
                        plane_ = jet(random.randint(1,2), bms, aburn)
                        planes.append(name)
                        planes.append(plane_)
                        print(f"{name} added to my planes")

                    elif a_type == "4":
                        print("quiting")
                        break
        elif inp == "2":
            for i in range(len(planes)):
                if i % 2 == 0:
                    print("--------------------------------------------------------------------------------------------------------------------------------")
                    print("--------------------------------------------------------------------------------------------------------------------------------")
                    print(planes[i])
                elif 1 % 2 != 0:
                    planes[i].get_info()
        elif inp == "3":
            print("what aircraft do you want to use")
            for i in range(len(planes)):
                if i % 2 == 0:
                    print(planes[i])
                else:
                    planes[i].get_info()
                uinp = input()
            for i in range(len(planes)):
                if planes[i] == uinp:
                    my_plane = planes[i+1]
                    break
                else:
                    pass
            print("What action would you like to preforme?")
            if type(my_plane) == jet:
                if my_plane.in_air == False and my_plane.on_runway == True:
                    print("1. normal take-off")
                    print("2. preformance take-off")
                    uinp = input()
                    if uinp == "1":
                        my_plane.fly()
                    elif uinp == "2":
                        my_plane.fly()
                elif my_plane.in_air == False and my_plane.on_runway == False:
                    if my_plane.power == True:
                        print("1. taxi to the runway")
                        print("2. shutdown")
                    elif my_plane.power == False:
                        print("1. startup")
                elif my_plane.in_air == True:
                    print("1. defend")
                    print("2. drop bombs")
                    print("3. shoot")
            elif type(my_plane) == cargo:
                print("defend")
                print("2. drop cargo")
            elif type(my_plane) == civ:
                
        else:
            print("invalid input pleas try again :<")
            print()
except:
    print("uh-oh somthing went wrong")