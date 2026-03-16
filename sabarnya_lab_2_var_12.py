print(issubclass(bool, int)) # True
print(issubclass(float, int)) # False
print(issubclass(int, float)) # False
print(issubclass(complex, type)) # False
print(issubclass(complex, object))
class Base(object): pass
class Child(object): pass
print(issubclass(Child, Base)) # True
print(issubclass(Base, object)) # True
print(issubclass(Child, object)) # True по транзитивности
