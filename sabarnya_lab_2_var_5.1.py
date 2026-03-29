class Transport:
    pass
class Land(Transport):
    def get_info(self):
        return "це наземний транспорт"
class Water(Transport):
    def get_info(self):
        return "це водний транспорт"
class Auto(Land):
    pass
class Boat(Water):
    pass
class Gibrid(Land, Water):
    def get_info(self):
        return "це гібридний транспорт"


boat = Boat()
gibrid = Gibrid()
auto = Land()
print(f"Boat: {boat.get_info()}")
print(f"Gibrid: {gibrid.get_info()}")
print(f"Auto: {auto.get_info()}")
