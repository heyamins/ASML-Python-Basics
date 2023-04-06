
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Vector({self._x}, {self._y})'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)


if __name__ == '__main__':


    v1 = Vector(5, 5)
    v2 = Vector(-3, 4)

    print(v1)
    print(v2)

    v3 = v1 + v2

    print(v3)
