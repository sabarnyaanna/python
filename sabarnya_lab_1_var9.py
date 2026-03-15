class Complex:
    """Комплексне число"""

    def __init__(self, real=0.0, imaginary=0.0):
        """Конструктор"""
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        """Опис об'єкта"""
        return 'Complex(%g, %g)' % (self.real, self.imaginary)

    def __str__(self):
        """Рядкове представлення"""
        return '%g %c %gi' % (
            self.real,
            '+' if self.imaginary >= 0 else '-',
            abs(self.imaginary)
        )

    # Арифметичні операції
    def __add__(self, other):
        """Додавання"""
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __neg__(self):
        """Заперечення"""
        return Complex(-self.real, -self.imaginary)

    def __sub__(self, other):
        """Віднімання"""
        return self + (-other)

    def __abs__(self):
        """Модуль числа"""
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    # Операції порівняння
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return not (self == other)


def main():
    x = Complex(2, 3.5)
    print(repr(x))
    print("x =", x)

    y = Complex(5, 7)
    print("y =", y)

    print("x + y =", x + y)
    print("x - y =", x - y)

    print("|x| =", abs(x))
    print("(x == y) =", x == y)


if __name__ == "__main__":
    main()