
class Person:

    __slots__ = ('name', 'residence')

    def __init__(self, name, residence = 'unknown'):
        self.name = name
        self.residence = residence

    def tell(self):
        return f'I am {self.name} and I live in {self.residence}'

    def move(self, new_residence):
        self.residence = new_residence


# -------------------------------

# Instantiation - creating an object
p1 = Person('Peter', 'Lhee')

p2 = Person('Ying Hsuan')

print(p1.tell())
print(Person.tell(p1))

print(p2.tell())

#
#
# p1.move('Eindhoven')
# print(p1.tell())
