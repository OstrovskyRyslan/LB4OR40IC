from services.hero import Hero

class LegendHunter(Hero):
    def __init__(self):
        super().__init__()
        self._power = 2
        self._speed = 3
        self._defense = 0

    def getName(self):
        return "Legend Hunter"
