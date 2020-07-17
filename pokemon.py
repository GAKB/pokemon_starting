# Define Pokemon class
class Pokemon():
    def __init__(self, name, level, element):
        self.name = name
        self.level = level
        self.element = element
        self.max_health = level
        self.health = level
        self.status = "active"
    def knock_out(self):
        self.status = "knocked out"
        print("{} has {} health left and is {}! \n".format(self.name, self.health, self.status))
    def wound(self, damage):
        if self.status == "knocked out":
            return print("{} is {}!".format(self.name, self.status))
        if damage >= self.health:
            print("{} has taken {} wounds.".format(self.name, damage))
            self.health = 0
            self.knock_out()
        else:
            self.health = self.health - damage
            print("{} has taken {} wounds and has {} health remaining. \n".format(self.name, damage, self.health))
    def heal(self, amount):
        if self.status == "knocked out":
            return print("{} is {}!".format(self.name, self.status))
        if self.health + amount >= self.max_health:
            self.health = self.max_health
            print("{} has healed fully and has {} health! \n".format(self.name, self.health))
        else:
            self.health = self.health + amount
            print("{} has healed {} and now has {} health remaining. \n".format(self.name, amount, self.health))
    def revive(self):
        if self.status == "knocked out":
            self.status = "active"
            self.health = self.max_health
            print("{} has been revived and has {} health! \n"
                  .format(self.name, self.health))
    def attack(self, opponent):
        if opponent.status == "Knocked out":
            print("{} is {}! They cannot be attacked. \n"
                  .format(opponent.name, opponent.status))
        else:
            damage_multiplier = {"FireFire": 1/2,
                                 "FireWater": 1/2,
                                 "FireGrass": 2,
                                 "WaterWater": 1/2,
                                 "WaterFire": 2,
                                 "WaterGrass": 1/2,
                                 "GrassGrass": 1/2,
                                 "GrassFire": 1/2,
                                 "GrassWater": 2}
            combat_elements = self.element + opponent.element
            damage = self.level * damage_multiplier[combat_elements]
            if damage_multiplier[combat_elements] == 2:
                print("{} is attacking {}. \n{} has advantage over {}, \n{} deals double damage!"
                      .format(self.name, opponent.name, self.element, opponent.element, self.name))
            if damage_multiplier[combat_elements] == 1/2:
                print("{} is attacking {}. \n{} has a disadvantage over {}, \n{} deals half damage."
                      .format(self.name, opponent.name, self.element, opponent.element, self.name))
            opponent.wound(damage)


# Define Trainer class




# Testing our class methods below
charmeleon = Pokemon("Charmeleon", 50, "Fire")
squirtle = Pokemon("Squirtle", 50, "Water")
tangela = Pokemon("Tangela", 50, "Grass")

charmeleon.attack(tangela)
charmeleon.attack(squirtle)
squirtle.attack(charmeleon)
tangela.revive()
tangela.attack(squirtle)

