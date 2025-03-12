class BaseBeast:

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

    def getInfo(self):
        print("\tІм'я: ", self.getName())
        print("\t", "Властивості: ")
        print("\t", "Сила: ", self.getPower())
        print("\t", "Швидкість: ", self.getSpeed())
        print("\t", "Захист: ", self.getDefense())

    def getType(self):
        return "коня"

    def getName(self):
        return "Скакун"

    def action(self):
        print(self.getName(), "посадив шукача пригод на плечі, та одним стрибком перестрибнув річку. Вони могли йти "
                              "далі")