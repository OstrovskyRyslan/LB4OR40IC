
class BasePotion:

    def __init__(self):
        self._power = 0
        self._speed = 0
        self._defense = 0


    def getPower(self):
        return self._power

    def getSpeed(self):
        return self._speed

    def getDefense(self):
        return self._defense