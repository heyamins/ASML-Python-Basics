
class ParentA:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

class ParentB:
    def __init__(self, d, e, f):
        self._d = d
        self._e = e
        self._f= f

class Child(ParentA, ParentB):
    def __init__(self, a, b, c, d, e, f):
        ParentA.__init__(self, a, b, c)
        ParentB.__init__(self, d, e, f)


child = Child(1, 2, 3, 4, 5, 6)

print(child)
