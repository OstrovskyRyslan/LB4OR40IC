from services.main_way import MainWay
from equipment.spear import Spear
from beast.base_beast import BaseBeast
from beast.animal import Animal
from beast.wolf import Wolf
from services.legendhunter import LegendHunter 
from services.maelor import Maelor
from services.thief import Thief
from beast.river import River
from beast.energy import Energy
from magic_potion.powerpotion import PowerPotion 

# Створення головного героя
hero = LegendHunter()

# Створення об'єктів
beast = BaseBeast()
animal = Animal()
wolf = Wolf()
maelor = Maelor()
river = River()
thief = Thief()
energy = Energy()

# Додаємо зілля та спорядження
hero.setPotion(PowerPotion())
hero.setEquipment(Spear())

# Головний шлях гри
main_way = MainWay(hero, beast, wolf, maelor, river, thief, energy, animal)
main_way.setInstruction("Довідка.")

# Запуск гри
main_way.run()
main_way.episode1()
main_way.episode2()
main_way.episode3()
main_way.episode4()
main_way.episode5()