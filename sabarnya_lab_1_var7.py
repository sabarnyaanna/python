class Rectangle:
    """Клас, який описує прямокутник"""

    def __init__(self, side_a, side_b):
        """Конструктор класу"""
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        """Повертає рядкове представлення об'єкта"""
        return 'Rectangle(%.1f, %.1f)' % (self.side_a, self.side_b)


class Circle:
    """Клас, який описує коло"""

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return 'Circle(%.1f)' % self.radius

    @classmethod
    def from_rectangle(cls, rectangle):
        """
        Фабричний метод.
        Створює коло, яке описане навколо прямокутника.
        """
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    circle1 = Circle(1)
    print(circle1)

    circle2 = Circle.from_rectangle(rectangle)
    print(circle2)


if __name__ == '__main__':
    main()