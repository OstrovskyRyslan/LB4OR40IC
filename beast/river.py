from beast.base_beast import BaseBeast

class River(BaseBeast):
    def __init__(self):
        super().__init__()
        self._name = "Річка"
        self._power = 100  
        self._speed = 100  
        self._defense = 0  

    def getName(self):
        return self._name

    def action(self):
        print(f"{self.getName()} перегороджує шлях героя. Йому потрібно її подолати!")
