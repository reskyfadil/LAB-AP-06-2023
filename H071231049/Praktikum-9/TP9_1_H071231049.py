class Human :
    def __init__(self, name, position, speed):
        self.name = name
        self._speed = speed
        self.__position = position

    def movement(self, direct):
        for i in direct:
            if i.lower() == "l":
                self.__position -= self._speed
            elif i.lower() == "r":
                self.__position += self._speed
            else:
                pass
    
    def set_position(self, position):
        self.__position = position
    
    def get_position(self):
        return self.__position
    
class Hero(Human):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target._health -= self._power

    def set_health(self, health):
        self._health = health

    def get_health(self):
        return self._health
    
    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed
    
    def set_armor(self, armor):
        self._armor = armor

    def get_armor(self):
        return self._armor

class Warior(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._power = 26
        self._armor = 30
        
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power

class Assassin(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._power = 35
        self.speed = 4

    def special(self, target):
        self._armor = 42
        self._power = 7
        target._health -= self._power

class Support(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health += 150
    
warrior = Warior("bambang", position=10, speed=3)
assassin = Assassin("joko", position=25, speed=9)
support = Support("udin",position=30, speed=9)
# sebelum
print("health (before)", warrior.get_health())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.get_health())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.get_health())
print("Support (speed) : ",support.get_speed())
print("-"*10)
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.get_health())
print("Support (speed): ",support.get_speed())
print("-"*20)
print(f"Posisi Warrior Sebelum berpindah : {warrior.get_position()}")
warrior.movement("LRLL")
print(f"Posisi Warrior Setelah berpindah : {warrior.get_position()}")







