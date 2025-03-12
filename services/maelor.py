from services.hero import Hero

class Maelor(Hero):
    def __init__(self):
        super().__init__()
        self._power = 1
        self._speed = 1
        self._defense = 1

    def getName(self):
        return "Maelor"
