class SuperComputer():
    def __init__(self, speed, agility):
        self.speed = speed
        self.agility = agility

    def display_attributes(self):
        print(self.speed, self.agility)

class MyPC(SuperComputer):
    def __init__(self,speed, agility, power):
        self.god_speed = speed
        self.god_agility = agility
        self.god_power = power
        super().__init__(1000,agility)

    def displayInfo(self):
        print(self.god_speed, self.god_agility, self.god_power)
    
intel = MyPC(200,"Not so good","200TB")
intel.display_attributes()
intel.displayInfo()
