class Hero:

    def __init__(self, magic_potion=None, equipment=None):
        if equipment is None:
            equipment = []
        if magic_potion is None:
            magic_potion = []

        self._power = 0
        self._speed = 0
        self._defense = 0

        self.magic_potion = []

        self._magic_power = 0
        self._magic_speed = 0
        self._magic_defense = 0

        self.equipment = []

        self.beast = []

        self._equipment_power = 0
        self._equipment_defense = 0

        self._beast_speed = 0

    def getPower(self):
        return self._power + self._magic_power + self._equipment_power

    def getSpeed(self):
        if self.beast is None:
            return self._speed + self._magic_speed + self._beast_speed
        else:
            return self._speed + self._magic_speed

    def getDefense(self):
        return self._defense + self._magic_defense + self._equipment_defense

    def setPotion(self, potion):
        if len(self.magic_potion) >= 2:
            print("\t", "Ви не можете взяти зілля більше, ніж дві пляшки")
            return True

        self.magic_potion.append(potion)
        return True

    def getPotion(self):
        return self.magic_potion

    def deletePotion(self, index):
        del self.magic_potion[index]

    def setEquipment(self, equipment):
        self.equipment.append(equipment)
        return True

    def setBeast(self, beast):
        self.beast.append(beast)
        return True

    def getInfo(self):
        print("\tІм'я: ", self.getName())
        print("\tВластивості: ")
        print("\tСила: ", self.getPower())
        print("\tШвидкість: ", self.getSpeed())
        print("\tЗахист: ", self.getDefense())

        print("\tЗілля: ")
        potion = self.getPotion()
        for item in potion:
            print("\t", item.getName())


    def drinkPotion(self, potion):
        self._magic_power = potion.getPower()
        self._magic_speed = potion.getSpeed()
        self._magic_defense = potion.getDefense()

        return True


    def sayWin(self):
        print("Я переміг")

    def sayFailed(self):
        print("Я програв")


    def getEquipmentNames(self):
        return self.equipment[0].getName()

    def getName(self):
        return "Ім'я"