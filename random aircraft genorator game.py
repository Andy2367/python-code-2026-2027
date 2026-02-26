elif inp == "3":
    print("What action would you like to preforme?")
    if self.power == True:
        if self.in_air == True and self == class(mill):
            print("1. defend")
            print("2. land")
            if self == class(fighter):
                print("3. drop bombs")
                print("4. shoot")
            elif self == class(cargo):
                print("2. drop cargo")
        elif self.in_air == True and self == class(civ):
            print("1. surve food")
            print("2. land")
        elif self.in_air == False and self == class(mill):
            if self.on_runway == True:
                print("1. standard take-off")
                print("2. preformance take-off")
            elif self.on_runway == False:
                print("1. taxi to runway")
                print("2. shut down")
        elif self.in_air == False and self == class(civ):
            if self.on_runway == True:
                print("1. reduced power take-off")
                print("2. Toga take-off")
            elif self.on_runway == False:
                print("1. taxi to runway")
                print("2. shutdown")
    elif self.power == False:
        print("1. start aircraft")
        print("2. quit")