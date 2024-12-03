# Задача "Ошибка эволюции"

from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            return
        # self._cords = list(map(lambda cord_val: self.speed * cord_val, (dx, dy, dz)))
        # add new functionality
        # self._cords = list(cur_cord + dcord for cur_cord, dcord in
        #                    zip(self._cords,
        #                        map(lambda cord_val:
        #                            self.speed * cord_val, (dx, dy, dz))))
        # more readable and efficient, plus new functionality
        for i, dcord in zip(range(3), (dx, dy, dz)):
             # self._cords[i] += dcord * self.speed
             self._cords[i] = dcord * self.speed

    def get_cords(self):
        # print(', '.join(f'{cord_title}: {cord_val}' for cord_title, cord_val in
        #                 zip(('X','Y','Z'), self._cords)))
        # more readable and efficient
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= int(abs(dz) * self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
