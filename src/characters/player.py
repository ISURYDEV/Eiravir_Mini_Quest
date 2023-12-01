class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.magic_power = 0
        self.mana = 0

    def display_stats(self):
        print(f"{self.name} - Level {self.level} {self.character_class}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Magic Power: {self.magic_power}")
        print(f"Mana: {self.mana}")

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, "Warrior")
        self.health += 100
        self.attack += 15
        self.defense += 10

class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage")
        self.health += 60
        self.attack += 5
        self.magic_power += 20
        self.mana += 25

class Archer(Player):
    def __init__(self, name):
        super().__init__(name, "Archer")
        self.health += 80
        self.attack += 10
        self.defense += 5