from services.hero import Hero

class Thief(Hero):
    def __init__(self):
        super().__init__()
        self._power = 1
        self._speed = 10
        self._defense = 0

    def getName(self):
        return "Thief"
