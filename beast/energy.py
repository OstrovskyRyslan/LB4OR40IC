from beast.base_beast import BaseBeast

class Energy(BaseBeast):
    def __init__(self):
        super().__init__()
        self._name = "Енергетичний бар'єр"
        self._power = 1000  
        self._speed = 1
        self._defense = 1000

    def getName(self):
        return self._name

    def action(self):
        print(f"{self.getName()} дає герою додаткову силу!")
