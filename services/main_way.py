import time

class MainWay:

    def __init__(self, legendhunter, beast, wolf, maelor, river, thief, energy, animal): 
        self.energy = energy
        self.thief = thief
        self.river = river
        self.maelor = maelor
        self.wolf = wolf
        self._opponent = None
        self._hero = legendhunter
        self._beast = beast
        self._opponent = wolf
        self.instruction = "Книга порожня"
        self.animal = animal

    def setInstruction(self, instruction):
        self.instruction = instruction

    def run(self):


        print("Привіт, шукач легенд, я Маелор. Тут починається твій шлях в загадковому світі Легендіуму.")
        print("")
        time.sleep(1)
        print("Легендіуму - це світ фантазії, сповнений міфічних істот, стародавньої магії та могутніх чарівників. ")
        print("Земля величезна і різноманітна, з високими горами, густими лісами, безкрайніми пустелями і блискучими ")
        print("океанами. Колись небом правили величні дракони, які з легкістю ширяли у хмарах і дихали полум'ям, ")
        print("здатним спопелити цілі армії. Тепер вони ширяють тільки у легендах, що переказують у своїх піснях "
              "хмільні барди")
        print("")
        input("Enter - продовжити...")
        print("Магія Легендіуму є водночас дивовижною та небезпечною. Нею володіють добрі чарівники, ")
        print("які використовують свої сили, щоб захистити землю та її мешканців від лиха. Але є й злі чарівники, ")
        print("які прагнуть отримати владу за будь-яку ціну і не зупиняються ні перед чим для досягнення своїх цілей.")
        print("")
        input("Enter - продовжити...")
        print("Незважаючи на наявність добра і зла, жителі Легендіуму стійкі і хоробрі, і об'єдналися для боротьби з ")
        print("темрявою. Вони - вправні воїни, хитрі шукачі пригод і спритні торговці, які використовують свої ")
        print("унікальні таланти, щоб захистити свої домівки та сім'ї.")
        print("")
        input("Enter - продовжити...")
        print("Але в тіні Легендіуму ховається похмура таємниця, яку мало хто наважується розкрити. Одні кажуть, ")
        print("що це прокляття, яке спіткало цю землю, інші вважають, що це могутній артефакт, який може перехилити ")
        print("баланс сил між добром і злом. Як би там не було, кажуть, що лише найсміливіші та найхитріші шукачі ")
        print("пригод зможуть розкрити правду і врятувати Легендіум від його долі.")

        print("...")
        print("...")

        self._name = input("Введіть свє ім'я: ")

        print("Маелор", ": Я дуже радий, що ти став на цей шлях. Легендіум сповнений леген, та э одна таэмниця, ")
        print("яку поховала під собою велична гора Дракона. Ніхто не зміг підібратися до неї, але ходять ")
        print("легенди, що то було в далекі часи драконів. Коли народжується дракон, земля викидає ріки ")
        print("лави, з тієї лави виринає промінь потужної енергії, що проходить крізь Місяць, та після з ")
        print("неба спускається дракон. Кх, так кажуть легенди, драконів ніхто не бачив вже тисячі років. ")
        print("Але те, що ти прийшов в наш світ одночасно з виверженням вулкану, не збіг, хтось розбудив ")
        print("гору, увесь світ в небезпеці... Так каже проротство...")
        print("")
        print(self._name, ": - ", "Що за проротство?")

        input("Enter - продовжити...")
        print("Маелор", ": Проротцтво про наш світ, коли прийде лихо, то мужній воїн з'явиться, щоб врятувати його. ")
        print("Він перетне багато перешкод, але найголовнішими будуть моральні вибори, які треба буде ")
        print("зробити")
        print("")
        print("Маелор", ": Я все розповім, коли прийде час, а зараз нам потрібно поспішати, ти повинен навчитися жити в ")
        print("цьому світі.")

        print("Інструкція: ")
        print(self.instruction)
        input("Enter - продовжити...")
        print("")
        print("Маелор", ": Я все розповім, коли прийде час, а зараз нам потрібно поспішати, ти повинен навчитися жити в "
                        "цьому світі.")
        print("")
        time.sleep(1)
        print("Маелор", ": Ось трактат знань, в ньому є все щоб зрозуміти, як працює цей світ. І пам'ятай, "
                        "життя Легендіуму залежне від тебе так само, як і ти залежний від Легендіуму")
        print("")
        time.sleep(1)
        print("Маелор", ": Мені час, ми зустрінимося знов, коли прийде час.")

        input("Enter - продовжити...")

    def episode1(self):
        print()
        print("episode 1")
        print()
        print(self._name, ": - ", "Я не пам'ятаю, як я сюди потрапив, але я відчуваю, що я на своєму місці. ")

        input("Enter - продовжити...")

        print("Герой обернувся та побачив навколо себе ... ")

        print("")
        print("Коли головний герой обернувся, перед ним відкрилося захоплююче ")
        print("видовище, від якого перехоплювало подих. Вдалині височіли гори, засніжені вершини яких пронизували ")
        print("хмари. Їх оточували густі ліси, що кишіли життям і звуками птахів та тварин. Повітря було наповнене ")
        print("солодким ароматом польових квітів і шумом водоспаду неподалік. Придивившись ближче, головні герої ")
        print("помітили, що дерева і кущі були не схожі на ті, які вони бачили раніше. Деякі з них світилися ")
        print("потойбічним світлом, а інші, здавалося, рухалися за власним бажанням. Маленька істота, вдвічі менша за ")
        print("людину, промчала крізь гущавину, її крила билися так швидко, що розпливалися в повітрі.")
        print("")
        print("Поки він стояв, вбираючи все це в себе, то зрозумів, що він більше не перебуває у "
              "звичному для них світі, який він знав. він потрапили у світ магії та дива, сповнений пригод і "
              "небезпек, і його переповнювало хвилювання і трепет перед тим, що чекає на нього попереду.")
        print("")
        print(self._name, ": - ", "Треба піднятися на той пагорб, так я зможу побачити як пройти до гори, та куди "
                                  "тече лава.")

        input("Enter - продовжити...")

        print("Піднімаючись на пагорб", self._name, "побачив як за ним біжить вовк, що робити?")

        self._opponent = self.wolf
        self.action()
        print("")
        print("З пагорбу відкрився вид на всю долину перед горою. Вона була залита золотими променями сонця. Ці ")
        print("проміння відбивалися від спокійної річки, що текла через всю долину. В кінці долини починався ліс, ")
        print("за лісом височіла гора, яка відкидала тінь на свою північну сторону. Шукачу легенд здалося, ")
        print("що ця тінь на щось схожа, але не зрозуміло на що.")

    def episode2(self):
        print()
        print("episode 2")
        print()
        print("Земля затремтіла ...")
        input("Enter - продовжити...")

        print("У підніжжя гори, відразу за лісом із під-землі вирвався згусток чистої енергії, це було схоже на стовп ")
        print("світла, що вистрелює в небо, та пронзаючи хмари ховається поміж майже повного місяця.")
        print("")
        print(self._name, ": - ", "Це все схоже на легенду, яку розповідав Маелор, мені потрібно скоріше підійти "
                                  "ближце до того небезпечного місця.")

        input("Enter - продовжити...")
        print("Спускаючись з пагорбу, шукач легенд відчув це дивне почуття, на нього хтось дивився, але звідки?")

        print("Вор", " - Хлопчик вийшов не на той шлях? Здається, що мені потрібні твої гроші, хоча...")

        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Вор", " - .. мені потрібні всі твої речі. Знімай рюкзак, та без дурниць, я маю ножа!")

        self._opponent = self.thief
        self.action()
        print("")
        print("Вор:", "- Стій, я помилився, ти мужній воїн, відпусти мене і я ніколи більше не стану в тебе на ")
        print("дроозі. Ось тобі подарунок, стародавній пергамент, тут написані давні істини, він дуже цінний.")
        print("")
        print("Прочитавши стародавній пергамент, шукач легенд зрозумів, що цей згусток енергії вивільнить дракона, ")
        print("котрий знищить увесь світ Легендіуму")

    def episode3(self):
        print()
        print("episode 3")
        print()
        print("Підійшовши до річки, герой побачив ледь живого", self._beast.getType())
        print("Сподіваюся, що у мене є зілля зцілення, я повинен врятувати", self._beast.getType())
        input("Enter - продовжити...")
        # goto: halth beast

        print("Вилікувавши", self._beast.getType(), " герой трохи відійшов. ", self._beast.getType(), " встав, та повернувся до нього")
        print(self._beast.getName(), ": - Дякую за рятунок, тепер я твій друг навіки!")
        input("Enter - продовжити...")
        print()
        print("Я не можу перепливти цю річку, вода занадто холодна, а річка широка. Можливо я зможу використати",
              self._beast.getType(), ". ",
              self._beast.getName(),
              "Ти допоможеш мені перетнути цю річку?")

        print(self._beast.getName(), ": - Так, я зможу тобі допомогти")
        print(self._name, ": - ", "Давай переберемося через річку")
        self._hero.setBeast(self._beast)
        self._opponent = self.river
        self.action()

    def episode4(self):
        print()
        print("episode 4")
        print()
        print(self._name, ": - ", "Який старий ліс. Цим дубам не менше 1000 років.")

        print(self._beast.getName(), ": - Це Диволіс, раніше він був не таким занедбалим. Я пам'ятаю, що малим ходив ")
        print("до цілющого джерела, воно загоювало будь які рани з мить. Але після того як ")
        print("гора виринула із-під землі, він зник. Ліс змінився, ми перестали туди заходити, ")
        print("бо там посилилися зловісні тварі, але це найкоротший шлях до гори. Ми повинні ")
        print("пройти через ліс")
        print("")
        print("Ви зайшли до лісу, стара дрога вела проміж дерев та чагарників, заплутувалася ярами та пагорбами, ")
        print("за декілька годин шляху ви вже не бачили ні кінця, ні краю цього лісу.")
        print("")
        print("Перед вами виринув вовк, він гнався за вами на пагорбі, та ось, напевно, наздогнав.")
        print("Ви дістали свій", self._hero.getEquipmentNames(), ", ви готові до битви")
        print("")
        self._opponent = self.wolf
        self.action()

        print(self._name, ": - ", "Це було складно, але я впорався")

        print("Удар, поштовх, ви падаєте з ніг. Вовк підходить попереду. Темрява закутує ваші очі... ледь чутні слова ")
        print("долинають до вас... ")
        print("")
        print("Вовк: - Я вже занадто довго на вас чекаю, чому ви йшли так довго.")
        print(self._beast.getName(), ": - Я плутав шлях, шукач легенд не повинен покинути цей ліс, це занадто ")
        print("небезпечно, ми не можемо ризикувати.")
        print("")
        print("Ви розплющуєте очі, туга потужка стягує ваші руки та ноги, ви сидите обперті об дерево, перед вами ")
        print("горить багаття, поряд нікого не видно. Далекі голоси чути із-за дерев...")
        print("")
        print(self._beast.getName(), ": - Маелор, так не можна, ти обіцяв, ти обіцяв зупинити пророцтво, якщо ми ")
        print("спіймаємо шукача легенд. Наш світ не може загинути")
        print("")
        print("Маелор", ": - ", self._beast.getName())
        print(", ти дурень, наш світ вже загинув, пророцтво не зупинити. На руїнах старого світу Я ... кхм, ")
        print("кхм. Ми збудуємо новий світ, кращий, світ, в якому будемо правити. Нам залишилося лише отримати силу ")
        print("дракона. І це станеться незабаром. Мені потрібно поспішати, скоро все скінчиться, цей кінець покладе ")
        print("новий початок, нову еру Легендіуму")
        print("")
        print("Маелор", ": - Вовк, ти підеш зі мною.", self._beast.getName(), ", стережи шукача легенд, він повинен ")
        print("залишитися в лісі за будь-якої ціни.")
        print("")
        print("Маелор, підходить до шукача легенд.")
        print("")
        print("Маелор", ": - ", self._hero.getName(), ", я казав, що ми зустрінемося знов. Дивись, ти будеш першим ")
        print("свідком нової ери.")
        print("")
        print("Маелор та вовк зникають між дерев, вони пішли в напрямку гори Дракона")
        print("")
        print(self._beast.getName(), ": - ", self._hero.getName(), ", Ми повинні їх зупинити, я знаю, що ти не можеш ")
        print("довіряти мені, але у тебе немає вибору. Хутчіш, ")
        print("ми повинні встигнути до святині скоріше за них.")

        print(self._beast.getName(), " розв'язує тебе, і ви поспішаєте до місця...")

    def episode5(self):
        print()
        print("episode 5")
        print()
        print("Святиня")
        print("")
        print("Ви бачите святиню, це ....")
        print("Це святиня Дракона")
        print("У світі Legendium Драконяче святилище - це священне місце, присвячене поклонінню драконам, ")
        print("яких шанують як могутніх і містичних істот. Ці святилища часто розташовані у віддалених і прихованих ")
        print("місцях, наприклад, глибоко в лісі, на вершині гори або в печері під землею.")
        print("")
        print("Коли головні герої наблизилися до святилища Дракона, вони побачили, що перед ними височіє споруда з ")
        print("каменю та мармуру. Храм мав велику залу з високими стелями, а зсередини долинали звуки співу та співів.")
        print("")
        print("Біля неї розгорнувся двобій, Маелор б'ється з хранителькою святині. Це ... Азура")
        print("")
        print("У святилищі Дракона в Легендіумі був могутній і мудрий охоронець, який відповідав за захист святині та ")
        print("її скарбів. Цю охоронницю звали Азура, і вона була жінкою великої сили, розуму та майстерності. Азура ")
        print("була вправним бійцем, а її майстерне володіння бойовими мистецтвами та зброєю робило її грізним ")
        print("супротивником для будь-кого, хто наважувався загрожувати святині Дракона. Вона також була вправним ")
        print("стратегом, з глибоким розумінням політики та боротьби за владу у світі Легендіуму. Як охоронниця ")
        print("Драконячої святині, Азура відповідала за збереження священного балансу між драконами та світом ")
        print("смертних. Вона служила посередником між двома світами, і говорили, що вона могла спілкуватися з самими ")
        print("драконами, отримуючи їхні настанови та мудрість.")
        print("")
        print( "Азура: Шукач легенд, ти вчасно, нам потрібна твоя допомога. Скоріш біжи в святиню, ти зрозумієш як ")
        print("зупинити все.")
        print("Маелор, ні, Вовк, зупини його.")
        print("")
        print("Попереду вас вистрибнув вовк, вам треба щось робити.")

        self._opponent = self.wolf
        self.action()

        print("Ви забігаєте до святині, на стінах ви бачите фрески пророцтва. там зображена ваша перша зустріч з ")
        print("Маелором, річка, і ліс зображений як пастка. Неможливо, це неможливо.")

        print("Останню фреску зруйновато ударом Маелора, який випадково потрапив сюди під час двобою. Ви озираєтесь "
              "навколо, очі шукають підказку... Її немає")
        print("")
        print(self._beast.getName(), ": - ", self._hero.getName(), ", ")
        print("Це пророцтво знають з дитинства всі мешканці Легендіуму. Ти можешь зупинити зло. Силу дракона  повинен ")
        print("отримати ти. Ти повинен шагнути в  енергію. Ти повинен довіритися зраднику. Ти повинен врятувати наш ")
        print("світ")
        self._opponent = self.energy
        self.action()

        print("Ви ступаєте в енергію. Ледь тепле світло окутує вас, все навколо заливає білий, як місячне сяйво, "
              "колір...")
        print("")
        print("Ви щось чуєте, якісь голоси.")
        print("")
        print("Голос: - ", self._name)
        print("Голос: - ", self._name)
        print("Голос: - ", self._name)
        print("...")

        print("Голос: - ", self._name, ", прокинься, онлайн урок вже починається, тобі потрібно підключитися до зуму.")
        print("...")
        input("Enter - продовжити...")

        print("Голос із зуму: - ", "Сьогодні ми продовжуємо вивчати ооп, та переходимо до тем...")
        print("Кінець")

    def action(self):
        print("")
        print("Ваші дії: ")
        self.writeCommands()
        command_str = input("Get command:")

        while command_str != 'next':
            if command_str == "get_info":
                self.getInfo()
            if command_str == "get_info_hero":
                self.getInfoHero()
            if command_str == "get_info_opponent":
                self.getInfoOpponent()
            elif command_str == "attack":
                resp = self.hero_attack()
                if resp:
                    break
            elif command_str == "run":
                resp = self.hero_run()
                if resp:
                    break
            elif command_str == "drink":
                self.hero_drink()

            command_str = input("Get command:")

    def writeCommands(self):
        print("\t", "get_info_hero", "-", "Отримати інформацію про героя")
        print("\t", "get_info_opponent", "-", "Отримати інформацію про опонента")
        print("\t", "attack", "-", "Атакуювати")
        print("\t", "run", "-", "Тікати")
        print("\t", "drink", "-", "Випити зілля")

    def getInfo(self):
        self._hero.getInfo()

    def getInfoOpponent(self):
        self._opponent.getInfo()

    def getInfoHero(self):
        self._hero.getInfo()

    def hero_attack(self):
        hero_attack = self._hero.getPower() - self._opponent.getDefense()
        opponent_attack = self._opponent.getPower() - self._hero.getDefense()

        if hero_attack > opponent_attack:
            self._hero.sayWin()
            return True
        else:
            self._hero.sayFailed()
            print("Yout hero is die")
            exit()

    def hero_run(self):
        hero_speed = self._hero.getSpeed() + self._beast.getSpeed()
        opponent_speed = self._opponent.getSpeed()

        if hero_speed > opponent_speed:
            self._hero.sayWin()
            return True
        else:
            self._hero.sayFailed()
            print("Yout hero is die")
            exit()

    def hero_drink(self):
        potion = self._hero.getPotion()
        count = len(potion)
        if count == 0:
            print("У вас немає зілля")
            return False
        print("Ваше зілля:")
        for item in range(count):
            print(item, potion[item].getName())

        number_potion = int(input("Введіть номер зілля, щоб випити: "))

        potion_use = potion[number_potion]

        self._hero.deletePotion(number_potion)

        self._hero.drinkPotion(potion_use)
