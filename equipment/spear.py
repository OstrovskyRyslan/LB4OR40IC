from equipment.base_equipment import BaseEquipment

class Spear(BaseEquipment):
    def __init__(self):
        super().__init__()
        self._power = 1  
        self._defense = 3 

    def getName(self):
        return "Спис"

    def attack(self):
        print(f"{self.getName()} завдає потужний удар! (+{self._power} до атаки)")

    def defence(self):
        print(f"{self.getName()} допомагає відбити атаку (+{self._defense} до захисту)")
