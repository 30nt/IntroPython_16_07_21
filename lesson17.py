class TD:
    def __init__(self, q, w, e):
        self.q = q
        self.w = w
        self._e = e


    def __repr__(self):
        return str(self.__dict__)

test_dict = TD("qwe", "asd", "zxc")
print(test_dict)

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.strength = 1
        self.agility = 1
        self.intelligence = 1


    def skill_up(self):
        print("hello")
        raise NotImplementedError

class Mage(Unit):
    # mage_type could be only "air", "fire", "water"
    def __init__(self, name, clan, mage_type: str):
        super().__init__(name, clan)
        self.mage_type = mage_type
        self.skill = 'intelligence'

    def skill_up(self):
        self.intelligence += 1

mage = Mage("jsdghf","kdfhv", "jdhgfbj")
mage.skill_up()
print(mage.intelligence)

from random import choice


class Unit:
    def __init__(self, name, clan):
        self._name = name
        self.clan = clan
        self._health = 100
        self._strength = 1
        self._dexterity = 1
        self._intelligence = 1
        self._base_skill = 1

    def __str__(self):
        return f"Персонаж:\nимя {self._name}, клан {self.clan}\n" \
               f"Характеристики: здоровье {self._health}" \
               f", сила {self.strength}, ловкость {self.dexterity}, интелект " \
               f"{self.intelligence} "

    def increase_health(self):
        if self._health <= 90:
            self._health += 10
        else:
            self._health = 100

    # @staticmethod
    # def _increase_skill(skill):
    #     if skill <= 9:
    #         skill += 1
    #     else:
    #         skill = 10
    #     return skill

    def increase_base_skill(self):
        if self._base_skill <= 9:
            self._base_skill += 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def strength(self):
        return self._strength

    @property
    def dexterity(self):
        return self._dexterity

    @property
    def intelligence(self):
        return self._intelligence


class Mage(Unit):
    def __init__(self, name, clan):
        super(Mage, self).__init__(name, clan)
        self._magic = choice(['воздух', 'огонь', 'вода'])

    def __str__(self):
        return f"{super().__str__()}, класс - маг, тип магии - {self._magic}"

    @property
    def magic(self):
        return self._magic

    @property
    def intelligence(self):
        self._intelligence = self._base_skill
        return self._intelligence



mage = Mage('Phess', 'Fireballs')
mage.increase_base_skill()
mage.increase_base_skill()
print(mage.intelligence)
