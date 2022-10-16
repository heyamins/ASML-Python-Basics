
class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Vector({self._x}, {self._y})'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __gt__(self, other):
        return self.length > other.length
    def __ge__(self, other):
        return self.length >= other.length
    def __lt__(self, other):
        return self.length < other.length
    def __le__(self, other):
        return self.length <= other.length
    def __eq__(self, other):
        return self.length == other.length
    def __ne__(self, other):
        return self.length != other.length

    @property
    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5


class Trajectory:

    def __init__(self):
        self._trajectory = []

    def append(self, vector):
        self._trajectory.append(vector)

    def __repr__(self):
        return repr(self._trajectory)

    @property
    def length(self):
        return sum(v.length for v in self._trajectory)

#---------------------------

v1 = Vector(3, 4)
v2 = Vector(-2, 6)

print(v1)
print(v2)

v3 = v1 + v2

v3 = Vector.__add__(v1, v2)

print(v3)

vectors = [v2, v3, v1]
print(vectors)

print(sorted(vectors))

t = Trajectory()
t.append(v1)
t.append(v2)
t.append(v3)
print(t)

print(v1.length)
print(v2.length)
print(v3.length)
print(t.length)