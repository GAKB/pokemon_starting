# Define Pokemon class
class Pokemon():
    def __init__(self,
                 name,
                 level,
                 element,
                 speed,
                 defense):
        self.name = name
        self.level = level
        self.element = element
        self.speed = speed
        self.defense = defense
        if level < 30:
            self.max_health = level + 30
        else:
            self.max_health = level + 20
        self.health = self.max_health
        self.status = "active"

    def __repr__(self):
        return ("Name: {}, \n  Level: {}, \n  Element: {}, \n  Speed: {}, \n  Defense: {}, \n  Health: {}, \n  Status: {}"
                .format(self.name, self.level, self.element, self.speed, self.defense, self.health, self.status))
        
    def knock_out(self):
        self.status = "knocked out"
        if self.health != 0:
            self.health = 0
        print("{} has {} health left and is {}! \n"
              .format(self.name, self.health, self.status))
        
    def wound(self, damage):
        if self.status == "knocked out":
            return print("{} is {}!"
                         .format(self.name, self.status))
        if damage >= self.health:
            print("{} has taken {} wounds.".format(self.name, damage))
            self.health = 0
            self.knock_out()
        else:
            self.health -= damage
            print("{} has taken {} wounds and has {} health remaining. \n"
                  .format(self.name, damage, self.health))
            
    def heal(self, amount):
        if self.status == "knocked out":
            return print("{} is {}!".format(self.name, self.status))
        elif self.health + amount >= self.max_health:
            self.health = self.max_health
            print("{} has healed fully and has {} health! \n"
                  .format(self.name, self.health))
        else:
            self.health += amount
            print("{} has healed {} and now has {} health remaining. \n"
                  .format(self.name, amount, self.health))
            
    def revive(self, heal):
        if self.status == "knocked out":
            self.status = "active"
            self.health = heal
            print("{} has been revived and has {} health! \n"
                  .format(self.name, self.health))
        else:
            print("{} is still {}, they cannot be revived!"
                  .format(self.name, self.status))
            
    def attack(self, opponent):
        if opponent.status == "knocked out":
            print("{} is {}! They cannot be attacked. \n"
                  .format(opponent.name, opponent.status))
        elif self.status == "knocked out":
            print("{} is {}! They cannot attack. \n"
                  .format(self.name, self.status))
        else:
            damage_multiplier = {"FireFire": 1,
                                 "FireWater": 1/2,
                                 "FireGrass": 2,
                                 "WaterWater": 1,
                                 "WaterFire": 2,
                                 "WaterGrass": 1/2,
                                 "GrassGrass": 1,
                                 "GrassFire": 1/2,
                                 "GrassWater": 2}
            combat_elements = self.element + opponent.element
            damage = self.level * damage_multiplier[combat_elements] - opponent.defense
            if damage_multiplier[combat_elements] == 2:
                print("{} is attacking {}. \n{} has advantage over {}, \n{} deals double damage!"
                      .format(self.name, opponent.name, self.element, opponent.element, self.name))
            if damage_multiplier[combat_elements] == 1/2:
                print("{} is attacking {}. \n{} has a disadvantage over {}, \n{} deals half damage."
                      .format(self.name, opponent.name, self.element, opponent.element, self.name))
            if damage_multiplier[combat_elements] == 1:
                print("{} is attacking {}. \n{} is equal to {}, \n{} deals normal damage."
                      .format(self.name, opponent.name, self.element, opponent.element, self.name))
            opponent.wound(damage)


# Define Trainer class
class Trainer():
    def __init__(self, name, pokemon_hand, potions):
        self.name = name
        self.potions = potions
        self.pokemon_hand = {pokemon.name: pokemon for pokemon in pokemon_hand}
        self.active = self.pokemon_hand[pokemon_hand[0].name]

    def __repr__(self):
        print("Trainer: {}".format(self.name))
        print("    Pokemon in hand:")
        for pokemon in self.pokemon_hand.keys():
            print("        {}".format(pokemon))
        print("    Potions in bag:")
        for potion in self.potions.keys():
            print("        {}".format(potion))

    def potion(self, potion):
        if potion not in self.potions:
            print("{} doesn't have a {} potion!".format(self.name, potion))
            if len(self.potions) > 0:
                print("    You have:")
                for key in self.potions.keys():
                    print("        {}".format(key))
            else:
                print("You have no potions left!")
        else:
            print("{} is using a {} potion.".format(self.name, potion))
            active_pokemon = self.active
            heal = self.potions[potion]
            if potion == "Revive":
                active_pokemon.revive(heal)
            else:
                active_pokemon.heal(self.potions[potion])
            self.potions.pop(potion)
        

    def fight(self, trainer):
        if self.active.status == "knocked out":
            print("{} is {}. {} cannot attack with this Pokemon."
                  .format(self.active.name, self.active.status, self.name))
        elif trainer.active.status == "knocked out":
            print("{} is {}. {} cannot be attacked."
                  .format(trainer.active.name, trainer.active.status, trainer.name))
        else:
            print("{} is starting a fight with {}. \n"
                  .format(self.name, trainer.name))
            if self.active.speed > trainer.active.speed:
                print("{} is faster and attacks first."
                      .format(self.active.name))
                self.active.attack(trainer.active)
                trainer.active.attack(self.active)
            elif self.active.speed < trainer.active.speed:
                print("{} is faster and attacks first.".format(trainer.active.name))
                trainer.active.attack(self.active)
                self.active.attack(trainer.active)

    def switch(self, name):
        if name in self.pokemon_hand and self.pokemon_hand[name].status == "knocked out":
            print("{} is knocked out! Choose another Pokemon from your hand:".format(name))
            print("You have:")
            for pokemon in self.pokemon_hand.keys():
                if self.pokemon_hand[pokemon].status == "active":
                    print("    {}".format(pokemon))
        elif name in self.pokemon_hand:
            self.pokemon_hand[self.active.name] = self.active
            self.active = self.pokemon_hand[name]
            print("{} has switched their active Pokemon to:".format(self.name))
            print(self.active, "\n")
        else:
            print("{} is not in your hand!".format(name))
            print("You have:")
            for pokemon in self.pokemon_hand.keys():
                if self.pokemon_hand[pokemon].status == "active":
                    print("    {}".format(pokemon))


# Assign Pokemon class objects
charmander = Pokemon("Charmander", 10, "Fire", 5, 2)
charmeleon = Pokemon("Charmeleon", 32, "Fire", 1, 1)
vulpix = Pokemon("Vulpix", 11, "Fire", 4, 2)
starmie = Pokemon("Starmie", 28, "Water", 2, 1)
poliwag = Pokemon("Poliwag", 13, "Water", 4, 2)
magikarp = Pokemon("Magikarp", 8, "Water", 5, 2)
staryu = Pokemon("Staryu", 15, "Water", 4, 2)
bulbasaur = Pokemon("Bulbasaur", 13, "Grass", 3, 2)
kakuna = Pokemon("Kakuna", 23, "Grass", 3, 2)
nidoran = Pokemon("Nidoran", 20, "Grass", 4, 1)
tangela = Pokemon("Tangela", 8, "Grass", 5, 2)
weedle = Pokemon("Weedle", 12, "Grass", 4, 2)


# Assign Trainer class objects
tony = Trainer("Tony",
                   [charmeleon, poliwag, tangela, weedle, bulbasaur, staryu],
                   {"Revive": 20, "Heal 20": 20, "Heal Max": 60, "Heal 30": 30})

thomas = Trainer("Thomas",
                   [charmander, vulpix, starmie, magikarp, kakuna, nidoran],
                   {"Revive": 20, "Heal 20": 20, "Heal Max": 60, "Heal 30": 30})

# Test Trainer and Pokemon methods
tony.fight(thomas)
thomas.fight(tony)
tony.potion("Heal 20")
thomas.switch("Starmie")
tony.fight(thomas)
tony.potion("Revive")
tony.switch("Tangela")
thomas.fight(tony)

