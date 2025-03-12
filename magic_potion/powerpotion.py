from magic_potion.base_potion import BasePotion

class PowerPotion(BasePotion):
    def __init__(self):
        super().__init__()
        self._power = 3  
        self._speed = 5
        self._defense = 100 

    def getName(self):
        return "Зілля Сили"

    def action(self):
        print(f"{self.getName()} випито! Герой отримує +{self.getPower()} до сили та +{self.getDefense()} до захисту!")
