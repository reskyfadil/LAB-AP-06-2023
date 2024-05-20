from hero import Warrior, Assassin, Support

warrior = Warrior("bambang", position=10)
assassin = Assassin("joko", position=25)
support = Support("udin", position=30)
# sebelum
print("health warrior:", warrior.get_health())
print("Assassin menyerang warrior")
assassin.attack(warrior)
# sesudah
print("health warrior setelah diserang assassin:", warrior.get_health())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.get_health())
print("Support (speed) default: ",support.get_speed())
print("support pake ulti ke warrior")
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.get_health())
print("Support (speed): ",support.get_speed())