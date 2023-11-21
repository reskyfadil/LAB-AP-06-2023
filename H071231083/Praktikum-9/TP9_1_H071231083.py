class Human:
    def __init__(self, name, position, speed=1): 
        self.name = name 
        self.__position = position 
        self._speed = speed 
        
    def Movement(self, arah):
        if arah == "R":
            self.__position += self._speed
        elif arah == "L":
            self.__position += self._speed
            
    def getPosition(self): 
        return self.__position
    def setPosition(self, position):
        self.__position = position
        
    def getSpeed(self):
        return self._speed
    def setSpeed(self, speed):
        self._speed = speed
        
class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def Attack(self, target):
        target._health -= self._power
        print(f"{self.name} Sedang Menyerang {target.name}, Health {target.name} berkurang sebanyak {self._power}, dan tersisa {target._health}")
    
    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def setPower(self, power):
        self._power = power
    def setHealth(self, health):
        self._health = health
    def setArmor(self, armor):
        self._armor = armor
    
class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30
        
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power
        print(f"{self.name} Sedang menggunakan special skill!")

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self._speed = 4
        
    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health = self._power
        print(f"{self.name} Sedang menggunakan special skill!")
        
class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health += 150
        print(f"{self.name} Sedang menggunakan special skill!")
    
warrior = Warrior("Ruby", 10)
assassin = Assassin("Saber", 25)
support = Support("Estes", 30)

#Sebelum
print(f"Darah {warrior.name} : ", warrior.getHealth())
assassin.Attack(warrior)
#Sesudah
print(f"Darah {warrior.name} :", warrior.getHealth())
print("-"*10)
#Sebelum
print(f"Darah {warrior.name} Saat ini :", warrior.getHealth())
print(f"Kecepatan {support.name} :", support.getSpeed())

support.special(warrior)
#Sesudah
print(f"Darah {warrior.name} Saat ini :", warrior.getHealth())
print(f"Kecepatan {support.name} : ", support.getSpeed())