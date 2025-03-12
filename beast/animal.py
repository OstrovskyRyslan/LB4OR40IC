from beast.base_beast import BaseBeast

class Animal(BaseBeast):
    def __init__(self):
        super().__init__()
        self._power = 1
        self._speed = 101
        self._defense = 0

    def getName(self):
        return "Тварина"

    def getType(self):
        return "Звір"

    def action(self):
        print(self.getName(), "готовий до подорожі з героєм!")
