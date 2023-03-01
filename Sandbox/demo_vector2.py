
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    @staticmethod
    def add_all(*vectors):
        v_sum = vectors[0]
        for v in vectors[1:]:
            v_sum = v_sum + v
        return v_sum

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, other):
        return self.length() == other.length()
    def __ne__(self, other):
        return self.length() != other.length()
    def __gt__(self, other):
        return self.length() > other.length()
    def __ge__(self, other):
        return self.length() >= other.length()
    def __lt__(self, other):
        return self.length() < other.length()
    def __le__(self, other):
        return self.length() <= other.length()

# ==========


v1 = Vector(5, 5)
v2 = Vector(-3, 4)

print(v1)
print(v2)

v3 = (((v1 + v2) + v2) + v2)

print(v3)

print(v1.length())
print(v2.length())
print(v3.length())

print(v1 > v2)

vectors = [v1,v2,v3]
print(sorted(vectors))

