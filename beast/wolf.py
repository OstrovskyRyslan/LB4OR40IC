from beast.base_beast import BaseBeast

class Wolf(BaseBeast):
    def __init__(self):
        super().__init__()
        self._power = 2
        self._speed = 1
        self._defense = 1

    def getName(self):
        return "Вовк"

    def getType(self):
        return "Хижак"

    def action(self):
        print(self.getName(), "випустив грізний рик і захистив героя!")
