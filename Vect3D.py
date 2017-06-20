class Vect3D:

    def __init__(self, x = 0, y = 0, z = 0):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = float(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = float(value)

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = float(value)

    # String represntation

    def __str__(self):
        return ("<%s, %s, %s>" % (self._x, self._y, self._z))

    # Produce a copy of itself
    def __copy__(self):
        return Vect3D(self._x, self._y, self._z)

    # Signing
    def __neg__(self):
        return Vect3D(-self._x, -self._y, -self._z)

    # Scalar Multiplication
    def __mul__(self, number):
        return Vect3D(self._x * number, self._y * number, self._z * number)

    def __rmul__(self, number):
        return self.__mul__(number)

    # Division
    def __div__(self, number):
        return self.__copy__() * (number**-1)

    # Arithmetic Operations
    def __add__(self, operand):
        return Vect3D(self._x + operand._x, self._y + operand._y, self._z + operand._z)

    def __sub__(self, operand):
        return self.__copy__() + -operand

    # Operations

    def normalize(self):
        return self.__div__(self.magnitude())

    def magnitude(self):
        return (self._x ** 2 + self._y ** 2 + self._z ** 2) ** (.5)

    # cross product
    def cross(self, operand):
        return Vect3D(self._y * operand.z - self._z * operand.y,
                      self._z * operand.x - self._x * operand.z,
                      self._x * operand.y - self._y * operand.x)

ZERO = Vect3D(0, 0, 0)